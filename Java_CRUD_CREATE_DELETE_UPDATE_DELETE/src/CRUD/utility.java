package CRUD;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.StringTokenizer;

public class utility {
    protected static boolean BukuAdaatauTidak(String[] keywords, boolean cek) throws IOException {
        FileReader fileinput = new FileReader("database.txt");
        BufferedReader buffread = new BufferedReader(fileinput);

        String data = buffread.readLine();
        boolean isExsist;
        int a = 0;
        while (data != null) { //perulangan mengecek data
            isExsist = true;
            for (String keyword : keywords) { //for each untuk mengulangi komponen dari si keywordS
                isExsist = (isExsist) && (data.toLowerCase().contains(keyword.toLowerCase()));
            } // menyamakan apakah keyword (komponen dari keywordS) ada didalam (data) dengan contains

            if (isExsist){ // jika true maka  data akan ditampilkan
                a++;
            }
            data = buffread.readLine(); // membaca baris pertama dan selanjutnya
        }

        if (a > 0 ){
            cek = false;
            System.out.println("data sudah ada!");
        } else {
            System.out.println("data belum ada");
            cek = true;
        }

        return cek;
    }

    // default access modifier
    static void cekDataBukuDiDatabase(String[] keywords) throws IOException{
        FileReader fileinput = new FileReader("database.txt");
        BufferedReader buffread = new BufferedReader(fileinput);

        String data = buffread.readLine();
        boolean isExsist;
        int nomorData = 0;
        int a = 0;

        System.out.println("| No |\tTahun |\t Penulis              |\tPenerbit             |\tJudul Buku");
        System.out.println("-----------------------------------------------------------------------------");
        while (data != null) { //perulangan mengecek data
            isExsist = true;
            for (String keyword : keywords) { //for each untuk mengulangi komponen dari si keywordS
                // perulangan akan terhenti jika komponen dari keywords habis
                isExsist = isExsist && data.toLowerCase().contains(keyword.toLowerCase());
                // mengecek adakah komponen dari keywords pada baris ini sebelum lanjut ke baris selanjutnya
                /*if (isExsist){
                    System.out.println("ini for each");
                } else {
                    System.out.println("ini bukan for each");
                }*/
            } // menyamakan apakah keyword (komponen dari keywordS) ada didalam data dengan contains
            if (isExsist){ // jika true maka  data akan ditampilkan
                a++;
                StringTokenizer fileToken = new StringTokenizer(data, ",");
                fileToken.nextToken();
                nomorData++;
                System.out.printf("|%2d  |", nomorData);
                System.out.printf("  %s  ",fileToken.nextToken());
                System.out.printf("|  %-20s | ",fileToken.nextToken());
                System.out.printf("%-20s |",fileToken.nextToken());
                System.out.printf("  %s  ",fileToken.nextToken());
                System.out.println();
            }
            data = buffread.readLine(); // membaca baris pertama dan selanjutnya
        }
        if ( a == 0){
            System.out.println("data tidak ditemukan");
        }
    }
    public static boolean getYesorNo(String message){
        Scanner pilihan = new Scanner(System.in);
        System.out.println(message);
        String input = pilihan.next();
        while (!input.equalsIgnoreCase("y") && !input.equalsIgnoreCase("n")){
            System.err.println("pilihan anda bukan y atau n");
            System.out.println(message);
            input = pilihan.next();
        }
        return input.equalsIgnoreCase("y"); // apabila input != y maka isilanjutkan nilainya false
    }
    public static void clearScreen(){
        try {
            if(System.getProperty("os.name").contains("Windows")){
                new ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();
            } else {
                System.out.println("\033\143");
            }
        }catch (Exception ex){
            System.err.println("tidak bisa melakukan clear screen");
        }
    }
}
