package lab01;

import lejos.hardware.Button;
import lejos.hardware.Sound;
import lejos.hardware.motor.EV3LargeRegulatedMotor;
import lejos.hardware.port.MotorPort;
import lejos.hardware.port.SensorPort;
import lejos.hardware.sensor.EV3TouchSensor;
import lejos.robotics.RegulatedMotor;
import lejos.robotics.SampleProvider;

public class SprintRace {
  public static void main(String[] args) {
    
    // set up motors
    RegulatedMotor left = new EV3LargeRegulatedMotor(MotorPort.A);
    RegulatedMotor right = new EV3LargeRegulatedMotor(MotorPort.B);

    // set up a touch sensor
    EV3TouchSensor touchSensor = new EV3TouchSensor(SensorPort.S1);
    SampleProvider touchSamplePr = touchSensor.getTouchMode();
    float[] touchSample = new float[touchSamplePr.sampleSize()];

    System.out.println("Push a button to start the sprint race!");
    Button.waitForAnyPress();

    while(true) {
      left.forward();
      right.forward();
      // stop and take a sample of the touch sensor
      touchSamplePr.fetchSample(touchSample, 0);
      System.out.println("Touch: " + touchSample[0]);
      // if touch sensor is being pushed, stop
      if(touchSample[0] == 1) {
          break;
      }
    }
    System.out.println("Finished the race");
    left.close();
    right.close();
    touchSensor.close();
    Sound.beepSequenceUp();

  }
}
