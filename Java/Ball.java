package balls;

import java.awt.*;
import java.util.Random;

import javax.swing.*;

public class Ball extends JComponent {
	// Private args
	private int x,y,radius;
	private int d_x, d_y, speed = 2, direction = 90;
	private Color color = Color.red;
	
	public Ball(int p_x, int p_y, int p_radius) {
		x 		= p_x;
		y 		= p_y;
		radius		= p_radius;
		updateDeplacement();
	}
	
	public void invertDx() {
		d_x = -d_x;
	}
	
	public void invertDy() {
		d_y = -d_y;
	}
	
	public void setColor(Color c) {
		color = c;
	}
	
	public void setSpeed(int sp) {
		speed = sp;
	}
	
	public void setDirection(int d) {
		direction = d;
		updateDeplacement();
	}
	
	public void updateDeplacement() {
		d_x = (int) (speed * Math.cos(direction));
		d_y = (int) (speed * Math.sin(direction));
	}
	
	public void paint(Graphics g) {
		super.paint(g);
		g.setColor(color);
	   	g.fillOval(x,y,radius,radius);
	}
	
	public void move() {
		x += d_x;
		y += d_y;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
	
	public int getRadius() {
		return radius;
	}
	
	public int getDx() {
		return d_x;
	}
	
	public int getDy() {
		return d_y;
	}
	
	
	
}
