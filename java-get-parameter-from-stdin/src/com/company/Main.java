package com.company;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        System.out.println("org");

        System.out.println(args.length);

        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }

        String[] reducedArgs = Arrays.copyOfRange(args, 1, args.length);

        System.out.println("new");

        System.out.println(reducedArgs.length);

        for (int i = 0; i < args.length; i++) {
            System.out.println(reducedArgs[i]);
        }

    }
}
