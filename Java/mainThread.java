package balls;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Scanner;

import javax.swing.*;

import balls.MainUI;

public class mainThread {

	public static void main(String[] args) {
		
		// Creation de la fenêtre
		MainUI UserInterface = new MainUI();
		BallGame game = new BallGame(UserInterface.ballArea);
		game.setScorePanel(UserInterface.score);
		Timer t = new Timer(UserInterface.timer);
		
		
		
		UserInterface.startStopButton.addActionListener(new ActionListener() {
		    public void actionPerformed(ActionEvent e)
		    {
		       if(UserInterface.startStopButton.getText().equals("START")) {
		    	   UserInterface.startStopButton.setText("STOP");
		    	   game.startGame();
		    	   t.startTimer();
		       } else {
		    	   UserInterface.startStopButton.setText("START");
		    	   game.stopGame();
		    	   t.stopTimer();
		       }
		    }
		});
		
		UserInterface.plusButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				game.addOneBall();
			}
		});
		
		UserInterface.resetButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				game.resetGame();
				t.resetTimer();
			}
			
		});
		
		UserInterface.minusButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				game.removeOneBall();
			}
		});
		
		
		
		
		game.start();
		t.start();
		
		
		
	}

}
