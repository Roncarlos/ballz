package balls;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;
import java.util.Vector;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class BallGame extends Thread {
	boolean running = false;
	BallsContainer ballsArea;
	JButton plusButton,minusButton,startStopButton;
	Random rModule = new Random();
	int addOneBall = 0;
	int deleteOneBall = 0;
	JLabel scorePanel;
	boolean reset = false;
	
	public BallGame(BallsContainer ballsArea) {
		this.ballsArea 			= ballsArea;
		this.setDaemon(true);
	}
	
	public void setScorePanel(JLabel score) {
		scorePanel = score;
	}
	
	public void startGame() {
		running = true;
	}
	
	public void stopGame() {
		running = false;
	}
	
	public void run() {
		try {
			while(true) {
				
				while(deleteOneBall > 0) {
					ballsArea.deleteBall();
					deleteOneBall--;
					ballsArea.repaint();
				}
				
				while(addOneBall > 0) {
					addOneBall--;
					int x = rModule.nextInt(ballsArea.getWidth());
					int y = rModule.nextInt(ballsArea.getHeight());
					// Radius 10 min 60 max
					int r = rModule.nextInt(50) + 40;
					if(x+r > ballsArea.getWidth()) x -= r;
					if(y+r > ballsArea.getHeight()) y -= r;
					Ball nBall = new Ball(x, y, r);
					nBall.setColor(new Color(rModule.nextInt(255), rModule.nextInt(255), rModule.nextInt(255)));
					nBall.setSpeed(rModule.nextInt(14) + 2);
					nBall.setDirection(rModule.nextInt(360));
					nBall.updateDeplacement();
					ballsArea.addBall(nBall);
					ballsArea.repaint();
				}
				
				if(running) {
					ballsArea.ballsCollision();
					ballsArea.moveBalls();
					scorePanel.setText("Score : " + ballsArea.score);
					ballsArea.repaint();
				}
				
				if(reset) {
					reset = false;
					ballsArea.reset();
				}
				
				sleep((long) 16.67);
			}
		} catch(InterruptedException e) {}
	}
	
	public void addOneBall() {
		if(!ballsArea.ballsFull()) {
			addOneBall += 1;
		}
	}
	
	public void removeOneBall() {
		if(ballsArea.atLeastOneBall()) {
			deleteOneBall++;
		}	
	}
	
	public void resetGame() {
		reset = true;
	}

}
