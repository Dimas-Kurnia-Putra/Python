package com.tutorial;

import java.io.*;
import java.util.Scanner;

// bilamana ingin mengambil fungsi dan class yang berbeda package maka import dahulu
// public dapat digunakan diluar package dengan mengimport package nya
// private dapat digunakan hanya dalam class yang sama
// protected dapat digunakan hanya dalam package yang sama
// default dapat digunakan hanya dalam package yang sama

import CRUD.operasi;
import CRUD.utility;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner terminalInput = new Scanner(System.in);
        String pilihan;
        boolean isiLanjutkan = true;

        while (isiLanjutkan) {

            System.out.println("Database Perpustakaan");
            System.out.println("\t1. Lihat data buku");
            System.out.println("\t2. Cari data buku");
            System.out.println("\t3. Tambah data buku");
            System.out.println("\t4. Ubah data buku");
            System.out.println("\t5. Hapus data buku");
            System.out.print("Masukan pilihan: ");
            pilihan = terminalInput.next();

            if (pilihan.equals("1")) {
                System.out.println("\n===============");
                System.out.println("LIHAT DATA BUKU");
                System.out.println("===============");
                operasi.tampilkanData();
            } else if (pilihan.equals("2")) {
                System.out.println("\n===============");
                System.out.println("CARI DATA BUKU");
                System.out.println("===============");
                operasi.cariData();
            } else if (pilihan.equals("3")) {
                System.out.println("\n===============");
                System.out.println("TAMBAH DATA BUKU");
                System.out.println("===============");
                operasi.tambahdata();
                operasi.tampilkanData();
            } else if (pilihan.equals("4")) {
                System.out.println("\n===============");
                System.out.println("UBAH DATA BUKU");
                System.out.println("===============");
                operasi.updatedata();
            } else if (pilihan.equals("5")) {
                System.out.println("\n===============");
                System.out.println("HAPUS DATA BUKU");
                System.out.println("===============");
                operasi.deletedata();
            } else {
                try {
                    System.err.println("anda salah input\ninput (1-5)!!!");
                    Thread.sleep(1000);
                }catch (InterruptedException ex){
                }
            }

            System.out.println();
            isiLanjutkan = utility.getYesorNo("apakah anda ingin melanjutkan? (y/n)");
            CRUD.utility.clearScreen();
        }
    }



}
