 prev_mod = 0;
 prev_x = 0;
 prev_y = 0;
 prev_z = 0;
 tol = 0.25;
 f1 = 0;
 f2 = 0;
 f3 = 0;
fs = 10000;
fc1 = 100;
t1 = 0:1/fs:5;
x1 = sawtooth(2*pi*fc1*t1);

while (1)

    mod = sqrt((x^2) + (y^2) + (z^2));
    if (abs(mod - prev_mod)>0.5)
        del_x = x - prev_x;%code to reevaluate direction
        del_y = y - prev_y;
        del_z = z - prev_z;
        if (abs(del_x)>tol && abs(del_y)<tol && abs(del_z)<tol)
            %ow
            f1 = 570;
            f2 = 840;
            f3 = 2410;

            if (del_x > 0)
                f = 880 + x*220;
            else
                f = 880 - x*220;
            end
           y1 = bandpass(x1,[f1-10 f1+10],fs) + bandpass(x1,[f2-10 f2+10],fs) + bandpass(x1,[f3-10 f4+10],fs);
           sound(y1,fs);
        end
        if (abs(del_y)>tol && abs(del_x)<tol && abs(del_z)<tol)
           %oo
            f1 = 300;
            f2 = 870;
            f3 = 2240;

            if (del_y > 0)
                f = 880 + y*220;
            else
                f = 880 - y*220;
            end
             y1 = bandpass(x1,[f1-10 f1+10],fs) + bandpass(x1,[f2-10 f2+10],fs) + bandpass(x1,[f3-10 f4+10],fs);
             sound(y1,fs);
        end
        if (abs(del_z)>tol)
            %a
            f1 = 730;
            f2 = 1090;
            f3 = 2440;

            if (del_z > 0)
                f = 880 + z*220;
            else
                f = 880 - z*220;
            end
            y1 = bandpass(x1,[f1-10 f1+10],fs) + bandpass(x1,[f2-10 f2+10],fs) + bandpass(x1,[f3-10 f4+10],fs);
            sound(y1,fs);
        end
        if (1-tol<del_x/del_y<1+tol)
            %ee
            f1 = 270;
            f2 = 2290;
            f3 = 3010;

            if (del_x > 0)
                f = 880 + x*220;
            else
                f = 880 - x*220;
            end
            y1 = bandpass(x1,[f1-10 f1+10],fs) + bandpass(x1,[f2-10 f2+10],fs) + bandpass(x1,[f3-10 f4+10],fs);
            sound(y1,fs);
        end
        if (-1-tol<del_x/del_y<-1+tol)
            %uh
            f1 = 520;
            f2 = 1190;
            f3 = 2390;

            if (del_x > 0)
                f = 880 + x*220;
            else
                f = 880 - x*220;
            end
            y1 = bandpass(x1,[f1-10 f1+10],fs) + bandpass(x1,[f2-10 f2+10],fs) + bandpass(x1,[f3-10 f4+10],fs);
            sound(y1,fs);
        end
    prev_mod = mod;
    prev_x = x;
    prev_y = y;
    prev_z = z;
   end
end





while (True)





    stream.write(sine)
end
