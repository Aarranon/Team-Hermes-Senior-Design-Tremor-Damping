Kp = 10
Ki = 1
Kd = 0.1
N = 100
f = 5
phase = 0;
tf1 = tf([1 0],[1 0 (2*pi*f)^2 ])
tf2 = tf([Kd * N 0],[1 N])
tf3 = tf([Ki],[1 0])
tf4 = tf1*(tf2+tf3+Kp)

pole(tf4)
bode(tf4)
