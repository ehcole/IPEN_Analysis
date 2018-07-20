import h5py
import numpy as np

#def print_attrs(name, obj):
 #   print(name)
  #  for key, val in obj.attrs.iteritems():
 #       print "    %s: %s" % (key, val)

if __name__ == '__main__':
    problem = "IPEN-005"
    filename = "%s.h5" % problem

  #  print filename
    f = h5py.File(filename, "r")
    #f.visititems(print_attrs)

    statename = "STATE_0001"
    ppstr = "pin_powers"

    groupname = "/%s/%s" % (statename,ppstr)

    pinpow = f[groupname]

    nx = 28
    ny = 28
    nz = 8
    na = 1

    #astt = [0,4,8,12]
    #astp = [4,8,12,16]
    astt = [0,3,6]
    astp = [3,6,9]

    nrows = 1

   # print pinpow 

    # pin boundaries: x index from 25 to 68
    #                 y index from  8 to 51
    #### convert powers to a 2D numpy array

    xstt = 0
    xstp = 27
    ystt = 0
    ystp = 27
    xsize = 28
    ysize = 28
    nz = 8

    rad_pow = np.zeros([xsize,ysize])
    power = np.zeros([xsize,ysize,nz])

    for z in range (0,nz):
        for j in range (0,nrows):
            for x in range (0,nx):
                global_x = (x+j*nx+1)
                if(global_x >= xstt and global_x < xstp):
             #       for a in range (astt[j],astp[j]):
                    a = 0
                    for y in range (0,ny):
                        global_y = (y+(a-astt[j])*ny+1)
                        if(global_y >= ystt and global_y < ystp):
                            #shift_x = global_x-xstt
                            #shift_y = ystp-global_y-1
                            shift_x = xstp-global_x-1
                            shift_y = global_y-ystt
                            power[shift_x,shift_y,z] = pinpow[x,y,z,0]

    for j in range (0,nrows):
        for x in range (0,xsize):
#            for a in range (astt[j],astp[j]):
            a = 0
            for y in range (0,ysize):
                powtemp = 0.0
                for z in range(0,nz):
                    powtemp = powtemp + power[x,y,z]
                rad_pow[x,y] = powtemp/float(nz)
                    
    #### normalize to (23,22)
    normpow = rad_pow[20,19]
    offset=3

    outfile = "%s.pinpow" % problem
    out = open(outfile,"w")
    out.write("      ")
    for x in range (0,xsize):
        powstring = "%7i" % (x+offset)
        out.write(powstring)
    out.write("\n")
    for y in range (0,ysize):
        powstring = "%-7i" % (y+offset)
        out.write(powstring)
        for x in range (0,xsize):
            powstring = "%.4f " % (rad_pow[x,y]/normpow)
            #powstring = "%.4f " % rad_pow[x,y]
            out.write(powstring)
        out.write("\n")
    out.close()
    f.close()

    #### check powers at specific coordinates
    npow = 5
    xcoord = [3,3,3,4,8,10,13,16,19,22,22,22,22]#,22,22,22,22,22,22,22,22,22,23,25,28,31,34,37,42,42]
    ycoord = [3,23,24,23,23,23,23,23,23,8,11,14]#,17,20,23,26,29,32,35,37,41,42,22,23,23,23,23,23,3,42]

    #### normalize to (23,22)
    normpow = rad_pow[20,19]

    #### print out table
    offset=3
    outfile = "%s.table" % problem
    out = open(outfile,"w")
    tabstring = "  x  |  y  |  power \n"
    for i in range(0,npow):
        x=xcoord[i]-offset
        y=ycoord[i]-offset
        tabstring = " %3i | %3i | %.4f \n" % (x+offset,y+offset,rad_pow[x,y]/normpow)
        out.write(tabstring)
    out.close
