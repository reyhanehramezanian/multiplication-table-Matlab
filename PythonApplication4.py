In general, the multiplication table in MATLAB looks like this:
n=input('entr the value:')
for i=1:n
    for j=1:n
        t(i,j)=i*j;
    end
end
disp(t);

For example, for the ten-by-ten multiplication table we have:
n=10
for i=1:10
    for j=1:10
       t(i,j)=i*j;
    end
end
disp(t);


