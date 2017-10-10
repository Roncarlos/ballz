package balls;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.border.*;

public class MainUI extends JFrame {
	
	// JPanels
	private JPanel content 			= new JPanel();
	private JPanel bottomConteneur 		= new JPanel();
	private JPanel topConteneur		= new JPanel();
	public BallsContainer ballArea		= new BallsContainer();
	
	/*
	 * Top Container Texts
	 */
	
	public JLabel score = new JLabel("Score : 0");
	public JLabel timer = new JLabel("00:00:00");
	
	/*
	 * Bottom Container Buttons
	 */
	public JButton startStopButton 	= new JButton("START");
	public JButton plusButton 		= new JButton("+");
	public JButton minusButton 		= new JButton("-");
	private JButton closeButton		= new JButton("CLOSE");
	public JButton resetButton 		= new JButton("RESET");
	
	public String START = "START";
	public String STOP  = "STOP";
	
	MainUI() {
		/*
		 * Screen size
		 * and set size 
		 * for elements
		 */
		Dimension screenSize 	= Toolkit.getDefaultToolkit().getScreenSize();
		double width 			= screenSize.getWidth();
		double height 			= screenSize.getHeight();
		
		Font buttonFont 		= new Font("Arial", Font.PLAIN, (int) ((width + height) / 2 * 0.03));
		int buttonWidth			= (int)( width * 0.125 );
		int buttonHeight		= (int)( height * 0.1 );
		
		Dimension buttonSize    = new Dimension(buttonWidth,buttonHeight);
		
		// Set window name
		setName("34003611 - Java Ball'z");
			
		// Set window size
		setSize(new Dimension((int) width, (int) (height)));
			
		// Prevent from resize
		setResizable(false);
				
		// Set full screen
		setExtendedState(Frame.MAXIMIZED_BOTH);
		setUndecorated(true);
				
		// Set visibility of screen to true
		setVisible(true);
				
		// Close default operation
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// JPanel set size
		bottomConteneur.setPreferredSize(new Dimension((int) width, (int)(height * 0.15)));
		topConteneur.setPreferredSize(new Dimension((int) width, (int)(height * 0.1)));
		ballArea.setPreferredSize(new Dimension((int) width, (int)(height * 0.75)));
		
		// Set backgrounds
		bottomConteneur.setBackground(new Color(122,122,122));
		topConteneur.setBackground(new Color(122,122,122));
		ballArea.setBackground(new Color(240,240,230));
		
		
		// layout set for all elements
		bottomConteneur.setLayout(new FlowLayout(FlowLayout.CENTER, 0, (int) (height*0.02)));
		
		topConteneur.setLayout(new BorderLayout());
		
		ballArea.setLayout(new GridLayout(1,1));
		
		/*
		 * Botton Conteneur
		 */
		
		// Button set size
		startStopButton.setPreferredSize(buttonSize);
		minusButton.setPreferredSize(buttonSize);
		plusButton.setPreferredSize(buttonSize);
		closeButton.setPreferredSize(buttonSize);
		resetButton.setPreferredSize(buttonSize);
		
		// Button set font size
		startStopButton.setFont(buttonFont);
		minusButton.setFont(buttonFont);
		plusButton.setFont(buttonFont);
		closeButton.setFont(buttonFont);
		resetButton.setFont(buttonFont);
		
		// Button part set position
		bottomConteneur.add(plusButton);
		bottomConteneur.add(minusButton);
		
		bottomConteneur.add(Box.createRigidArea(new Dimension( (int) (width / 2.75), 0)));
		
		bottomConteneur.add(resetButton);
		bottomConteneur.add(startStopButton);
		bottomConteneur.add(closeButton);

		
		/*
		 * Top container
		 */
		
		// set text size
		score.setFont(buttonFont);
		timer.setFont(buttonFont);
		
		topConteneur.setBorder(new EmptyBorder(0,(int)(width*0.1),0,(int)(width*0.1)));
		
		topConteneur.add(score, BorderLayout.LINE_START);
		topConteneur.add(timer, BorderLayout.LINE_END);
		
		
		/*
		 * Content container
		 */
		
		add(content);
		content.add(topConteneur, BorderLayout.PAGE_START);
		content.add(ballArea, BorderLayout.CENTER);
		content.add(bottomConteneur, BorderLayout.PAGE_END);
		
		
		// init listeners for buttons
		initListeners();
				
	}
	
	public JButton getPlusButton() {
		return plusButton;
	}
	
	public JButton getMinusButton() {
		return minusButton;
	}
	
	public JButton getStartStopButton() {
		return startStopButton;
	}
	
	public JPanel getBallsArea() {
		return ballArea;
	}
	
	private void initListeners() {
		
		/*
		 * Close Button Listener
		 * Just close the program
		 */
		closeButton.addActionListener(new ActionListener() {
		    public void actionPerformed(ActionEvent e)
		    {
		       dispose();
		    }
		});
		
		
	}

}
