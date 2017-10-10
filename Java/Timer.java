package balls;

import javax.swing.JLabel;

public class Timer extends Thread {
	int hours = 0, minutes = 0, seconds = 0;
	JLabel timerLabel;
	boolean running = false;
	
	public Timer(JLabel timerLabel) {
		setDaemon(true);
		this.timerLabel = timerLabel;
	}
	
	public void startTimer() {
		running = true;
	}
	
	public void stopTimer() {
		running = false;
	}
	
	public void resetTimer() {
		hours = 0;
		minutes = 0;
		seconds = 0;
		timerLabel.setText(getFormattedText());
	}
	
	public String getFormattedText() {
		String h = "00" , m = "00" , s = "00";
		if(seconds < 10) {
			s = "0" + seconds;
		} else {
			s = "" + seconds;
		}
		
		if(minutes < 10) {
			m = "0" + minutes;
		} else {
			m = "" + minutes;
		}
		
		if(hours < 10) {
			h = "0" + hours;
		} else {
			h = "" + hours;
		}
		return h + ":" + m + ":" + s;
	}
	
	public void run() {
		try {
			while(true) {				
				sleep(1000);
				if(running) {
					seconds++;
					
					if(seconds >= 60) {
						seconds = 0;
						minutes++;
					}
					
					if(minutes >= 60) {
						minutes = 0;
						hours++;
					}
					
					timerLabel.setText(getFormattedText());
				}
				
			}
		} catch (InterruptedException e) {}
	}
	
	
	
}
