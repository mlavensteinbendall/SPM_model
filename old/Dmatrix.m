Nsizes = 2000;

D1 = zeros(Nsizes);
D2 = zeros(Nsizes);

ds = 1;

D1(1,1) = -1/ds; 
D1(1,2) =  1/ds;

D2(1,1) =  1/(ds^2); 
D2(1,2) = -2/(ds^2); 
D2(1,3) =  1/(ds^2); 

for i = 2:Nsizes-1
   D1(i,i-1) = -0.5/ds; 
   D1(i,i+1) = 0.5/ds;

   D2(i,i-1) = 1/(ds^2); 
   D2(i,i) = -2/(ds^2); 
   D2(i,i+1) = 1/(ds^2);
end

D1(end,end-1) = -1/ds; 
D1(end,end)   =  1/ds; 

D2(end,end-2) =  1/(ds^2); 
D2(end,end-1) = -2/(ds^2); 
D2(end,end  ) =  1/(ds^2);

%%

Nsizes = 2000;

D1 = zeros(Nsizes);
D2 = zeros(Nsizes);

for i = 1:Nsizes-1
    D1(i,i) = -1;
    D1(i,i+1) = 1;
end

D1(end,end-1) = -1;
D1(end,end) = 1;

D2(1,1) = -1;
D2(1,2) =  1;
 
for i = 2:Nsizes

    D2(i,i-1) = -1;
    D2(i,i) = 1;

end

out = D1*D2;
