use pyo3::prelude::*;

#[pyclass]
pub struct HarmonicGearbox {
    kp: f64,
    ki: f64,
    kd: f64,
    integral: f64,
    prev_error: f64,
    status: String,
}

#[pymethods]
impl HarmonicGearbox {
    #[new]
    fn new(kp: f64, ki: f64, kd: f64) -> Self {
        HarmonicGearbox {
            kp,
            ki,
            kd,
            integral: 0.0,
            prev_error: 0.0,
            status: "⚙️ NORMAL".to_string(),
        }
    }

    fn tick(&mut self, dt: f64, input_freq: f64) -> f64 {
        // TARGET: The LuoShu Invariant
        let target = 15.0; 
        
        // 1. Error Calculation
        let error = target - input_freq;

        // 2. Integral (Faith/Flywheel)
        self.integral += error * dt;

        // 3. Derivative (Damping)
        let derivative = (error - self.prev_error) / dt;
        self.prev_error = error;

        // 4. PID Output
        let output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative);
        
        output
    }

    fn reset(&mut self) {
        self.integral = 0.0;
        self.prev_error = 0.0;
        self.status = "⚙️ NORMAL".to_string();
    }

    fn get_status_string(&self) -> String {
        self.status.clone()
    }

    fn engage_sovereign_override(&mut self, key: String) {
        if key == "OPHANE-X7" {
            self.status = "⚙️ SOVEREIGN".to_string();
        } else {
             self.status = "🚫 ACCESS DENIED".to_string();
        }
    }
}