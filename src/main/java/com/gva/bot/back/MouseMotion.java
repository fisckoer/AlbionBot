package com.gva.bot.back;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class MouseMotion {

    private Boolean botActivo = new Boolean(false);
    private Robot robot;

    private Random random;

    private int xInicial,xFinal,yInicial,yFinal;

    private JFrame jf;
    private JButton jButtonStart,jButtonArea;
    private JLabel jLabelXInicial,jLabelYInicial,jLabelXFinal,jLabelYFinal,jLabelValorX;


    public static void main(String args[]){
        new MouseMotion();
    }

    public MouseMotion(){
        try {
            robot = new Robot();
            random = new Random();
        } catch (AWTException e) {
            throw new RuntimeException(e);
        }
        jf = new JFrame("Albion Bot");
        jf.setBounds(0,0,200,400);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setLayout(null);
        jf.setLocationRelativeTo(null);
        jf.setResizable(false);
        ActionListener actionListener = getActionListener();
        jButtonStart = new JButton("Iniciar");
        jButtonStart.addActionListener(actionListener);
        jButtonStart.setBounds(40,300,120,20);
        jf.add(jButtonStart);
        jf.setVisible(true);
        MouseListener m = getMouseLitener();
        jf.addMouseListener(m);

    }

    private MouseListener getMouseLitener() {
        return new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {
                System.out.println("clic mouse");
                System.out.println(e.getX());
            }

            @Override
            public void mousePressed(MouseEvent e) {

            }

            @Override
            public void mouseReleased(MouseEvent e) {

            }

            @Override
            public void mouseEntered(MouseEvent e) {

            }

            @Override
            public void mouseExited(MouseEvent e) {

            }
        };
    }

    private ActionListener getActionListener() {
        return new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if(e.getSource()== jButtonStart){
                    if(!botActivo){
                        jButtonStart.setText("Detener");
                        botActivo =true;
                        mouseMove();
                    }else{
                        botActivo =false;
                        jButtonStart.setText("Iniciar");
                    }

                }
            }
        };
    }

    public void mouseGenerarClic(){

    }


    public void mouseMove(){
        if(botActivo) {
            Thread t1 = new Thread(getThread());
            t1.start();
        }
    }

    private Runnable getThread() {
        return new Runnable() {
            @Override
            public void run() {
                try{
                    Thread.sleep(1000);
                    int conta =0;
                    while(botActivo) {
                        int x = ThreadLocalRandom.current().nextInt(383, 983 + 1);// random.nextInt(983);
                        int y = ThreadLocalRandom.current().nextInt(284, 484 + 1);//random.nextInt(484);
                        robot.mouseMove(x,y);
                        System.out.println("cordenas de mouse click x:"+x+",  y:"+y);
                        robot.mousePress(InputEvent.BUTTON1_MASK);
                        Thread.sleep(4000);
                        //robot.mouseRelease(InputEvent.BUTTON1_MASK);
//                        conta++;
                    }
                }catch(InterruptedException e){}
            }
        };
    }
}
