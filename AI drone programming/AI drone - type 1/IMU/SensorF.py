import IMU10DOF
import IMU.SensorF as IMUSF

state_tm1 = IMUSF.state()
state_tm1.plot()
state_t = IMUSF.IMUSensorFusion(state_tm1, [0,0,0], [0,0,0], [0, 0, 0], [0, 0, 0], 0)
