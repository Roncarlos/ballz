package balls;

import java.awt.Graphics;
import java.util.Vector;

import javax.swing.JPanel;

public class BallsContainer extends JPanel {
	Vector<Ball> Balls = new Vector<Ball>();
	public int score   = 0;
	
	public void addBall(Ball b) {
		Balls.add(b);
	}
	
	public synchronized int getScore() {
		return score;
	}
	
	public void deleteBall() {
		Ball b = Balls.get(0);
		Balls.remove(b);
	}
	
	public void deleteThisBall(Ball b) {
		Balls.remove(b);
	}
	
	public boolean atLeastOneBall() {
		return Balls.size() > 0 ? true : false;
	}
	
	public boolean ballsFull() {
		return Balls.size() >= 20 ? true : false;
	}
	
	public void ballsCollision() {
		Vector<Ball> toDelete = new Vector<Ball>();
		for(Ball bPrincipal : Balls) {
			for (Ball bSecond : Balls) {
				if(!bPrincipal.equals(bSecond)) {
					double dx = bSecond.getX() - bPrincipal.getX();
					double dy = bSecond.getY() - bPrincipal.getY();
					int lRadius = bPrincipal.getRadius() > bSecond.getRadius() ? bPrincipal.getRadius() : bSecond.getRadius();
					double dist = Math.sqrt(dx *dx + dy * dy) - (lRadius);
							
					
					if(dist <= 0) {
						if(!toDelete.contains(bSecond))
							toDelete.add(bSecond);
						if(!toDelete.contains(bPrincipal))
							toDelete.add(bPrincipal);
					}
				}
			}
		}
		
		int tempScore = 0;
		for(Ball b : toDelete) {
			deleteThisBall(b);
			tempScore++;
		}
		
		if(tempScore > 0) {
			score += tempScore/2;
		}
		
	}

	public void moveBalls() {
		for(Ball b : Balls) {
			if(b.getX() <= 0 || b.getX() + b.getRadius() >= getWidth()) 
				b.invertDx();;
			if(b.getY() <= 0 || b.getY() + b.getRadius() >= getHeight())
				b.invertDy();
			b.move();
		}
		
	}
	
	public synchronized void reset() {
		Vector<Ball> toDelete = new Vector<Ball>();
		for(Ball b : Balls) {
			toDelete.add(b);
		}
		
		
		for(Ball b : toDelete) {
			deleteThisBall(b);
		}
		
		score = 0;
		repaint();
	}
	
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		for(Ball b : Balls) {
			b.paint(g);
		}
	}
}
