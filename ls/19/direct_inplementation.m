% system declaration:
A = [1 1; 0 1];
B = [0; 1];
C = [1 0];
% config:
x_0 = [1; 0];
rho = 0.1;
N = 20;
Q = rho*(C'*C);
R = 1;
% initial P - here is the 3-d matrix case
P(:,:, N) = Q;

for i = N-1:-1:1 % -1 is required for non +1 case
    P(:,:,i) = Q + A'*P(:,:,i+1)*A -...
        A'*P(:,:,i+1)*B*(R+B'*P(:,:,i+1)*B)^(-1)*B'*P(:,:,i+1)*A;
end
% get total cost
cost = x_0' * P(:,:,1) * x_0;
disp("cost is:");
disp(cost);
% here u is a scalar
x(:,:,1) = x_0;
u = zeros(1, N-1);
for t = 1:1:N-1
    u(:,t) = -(R + B'*P(:,:,t+1)*B)^(-1)*B'*P(:,:,t+1)*A*x(:,:,t);
    x(:,:,t+1) = A*x(:,:,t) + B* u(:,t);
end
plot(u);
disp("Finished!");
