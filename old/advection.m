ds = 0.01; 
dt = 0.9*ds;

slength = 30; 
tlength = 10; 

s = 0:ds:slength;
t = 0:dt:tlength; 

N(1:length(s)) = exp(-(s-10).^2); 

for i=1:length(t) 

    N(2:end) = N(2:end) - dt*(N(2:end)-N(1:end-1))/ds; 

    figure(1)
    hold off 
    plot(s,N,'k-')
    hold on 
    plot(s,exp(-(s-10-(i-1)*dt).^2),'r--')
    xlim([0,30])
    ylim([0,1])
    pause(0.1)


end


