package CRUD;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class operasi {
    public static void updatedata() throws IOException {
        // ambil database original
        File database = new File("database.txt");
        FileReader fileinput = new FileReader(database);
        BufferedReader buffread = new BufferedReader(fileinput);

        // buat database sementara
        File tempDB = new File("tempDB.txt");
        FileWriter fileoutput = new FileWriter(tempDB);
        BufferedWriter buffwrite = new BufferedWriter(fileoutput);

        // tampilkan datanya
        System.out.println("List Data");
        tampilkanData();

        // ambil user input
        Scanner terminalinput = new Scanner(System.in);
        System.out.println("masukan nomor buku yang akan diupdate: ");
        int updateNum = terminalinput.nextInt();

        String data;
        int entryCount = 0;

        while((data = buffread.readLine()) != null){
            entryCount++;

            StringTokenizer st = new StringTokenizer(data, ",");

            if (!data.isEmpty()) {
                // mengesekusi baris yang ingin di update
                if (updateNum == entryCount) {
                    // update
                    System.out.println("Data yang akan anda update adalah: ");
                    System.out.println("-----------------------------------");
                    System.out.println("referensi  :" + st.nextToken());
                    System.out.println("tahun      :" + st.nextToken());
                    System.out.println("penulis    :" + st.nextToken());
                    System.out.println("penerbit   :" + st.nextToken());
                    System.out.println("judul      :" + st.nextToken());

                    // mengambil input dari user
                    String[] fields = {"tahun", "penulis", "penerbit", "judul"};
                    String[] tempData = new String[4];

                    // refesh tokenizer
                    st = new StringTokenizer(data, ",");
                    String originaldata = st.nextToken();
                    for (int i = 0; i < fields.length; i++) {
                        boolean isupdate = utility.getYesorNo("apakah anda ingin merubah " + fields[i] + "? (y/n)");
                        originaldata = st.nextToken(); // data yang lama
                        if (isupdate) {
                            //user input
                            terminalinput = new Scanner(System.in);
                            System.out.println("masukan " + fields[i] + " baru: ");
                            tempData[i] = terminalinput.nextLine();
                        } else {
                            tempData[i] = originaldata;
                        }
                    }

                    // menampilkan data baru
                    st = new StringTokenizer(data, ",");
                    st.nextToken();
                    System.out.println("data baru anda adalah: ");
                    System.out.println("tahun      : " + st.nextToken() + " --> " + tempData[0]);
                    System.out.println("penulis    : " + st.nextToken() + " --> " + tempData[1]);
                    System.out.println("penerbit   : " + st.nextToken() + " --> " + tempData[2]);
                    System.out.println("judul      : " + st.nextToken() + " --> " + tempData[3]);

                    boolean isUpdate = utility.getYesorNo("apakah anda yakin ingin merubah data? (y/n)");
                    if (isUpdate) {
                        // cek daat baru di database ada atau tidak
                        boolean isexist = utility.BukuAdaatauTidak(tempData, false);
                        if (!isexist) {
                            System.out.println("silahkan hapus data terlebih dahulu");
                            buffwrite.write(data);
                        } else {
                            // format data ke database
                            String tahun = tempData[0];
                            String penulis = tempData[1];
                            String penerbit = tempData[2];
                            String judul = tempData[3];

                            // kita buat primarykey
                            String penuliswithoutspace = penulis.replaceAll("\\s+", "");
                            long nomorentry = 1;
                            String primarykey = penuliswithoutspace + "_" + tahun + "_" + nomorentry;
                            // tulis data baru ke database
                            buffwrite.write(primarykey + "," + tahun + "," + penulis + "," + penerbit + "," + judul);
                            System.out.println("data berhasil diUpdate!");
                        }
                    } else {
                        buffwrite.write(data);
                    }
                    System.out.println(Arrays.toString(tempData));
                } else {
                    // copy data
                    buffwrite.write(data);
                }
            } else {
                System.out.println("anda yang anda pilih kosong");
                System.out.println("silahkan ulangi program ini");
            }
            buffwrite.newLine();
        }

        buffwrite.flush();

        buffwrite.close();
        fileoutput.close();
        buffread.close();
        fileinput.close();

        // method dari kelas terbuka
        System.gc();

        // delete file original
        database.delete();

        // rename file temporary menjadi original
        tempDB.renameTo(database);
    }
    public static void deletedata() throws IOException{
        // kita ambil database original
        File database = new File("database.txt");
        FileReader fileinput = new FileReader(database);
        BufferedReader buffread = new BufferedReader(fileinput);

        // kita buat file sementara
        File temDB = new File("temDB.txt");
        FileWriter fileoutput = new FileWriter(temDB);
        BufferedWriter buffwrite = new BufferedWriter(fileoutput);

        // menampilkan data
        System.out.println("List Buku: ");
        tampilkanData();

        // mengambil input dari user untuk menghapus buku
        Scanner terminalinput = new Scanner(System.in);
        System.out.println("masukan nomor urutan buku yang akan dihapus: ");
        int deleteNum = terminalinput.nextInt();

        // looping untuk mengskip data yang akan dihapus
        int entrycount = 0;
        String data;
        while ((data = buffread.readLine()) != null){
            boolean isdelete = false;
            entrycount++;

            if (!data.isEmpty()) {
                if (deleteNum == entrycount) {
                    StringTokenizer st = new StringTokenizer(data, ",");
                    System.out.println("Ini data yang akan anda hapus");
                    System.out.println("-----------------------------");
                    System.out.println("referensi : " + st.nextToken());
                    System.out.println("tahun     : " + st.nextToken());
                    System.out.println("penulis   : " + st.nextToken());
                    System.out.println("penerbit  : " + st.nextToken());
                    System.out.println("judul     : " + st.nextToken());

                    isdelete = utility.getYesorNo("Apakah anda ingin menghapus data ini? (y/n)" +
                            "");
                }

                if (isdelete) {
                    // kita skip data yang akan dihapus
                    System.out.println("data berhasil dihapus");
                    System.out.println("\n");
                } else {
                    // kita tulis ulang data dari original ke sementara
                    buffwrite.write(data);
                    if (buffread.ready()) {
                        buffwrite.newLine();
                    }
                }
            } else {
                System.out.println("data yang akan dihapus kosong");
                System.out.println("silahkan ulangi program ini");
            }
        }
        // memindahkan data original ke sementara
        buffwrite.flush();

        buffwrite.close();
        fileoutput.close();
        buffread.close();
        fileinput.close();

        // method dari kelas terbuka
        System.gc();

        // delete file original
        database.delete();

        // rename file temporary menjadi original
        temDB.renameTo(database);

    }
    public static void tambahdata() throws IOException {
        FileReader fileinput = new FileReader("database.txt");
        FileWriter fileoutput = new FileWriter("database.txt", true);
        // append menambah data tanpa menghapus data sebelumnya

        BufferedReader buffread = new BufferedReader(fileinput);
        BufferedWriter buffwrite = new BufferedWriter(fileoutput);

        Scanner terminalinput = new Scanner(System.in);
        String penulis, judul, penerbit, tahun;

        System.out.print("masukan nama penulis: ");
        penulis = terminalinput.nextLine();
        System.out.print("masukan judul buku: ");
        judul = terminalinput.nextLine();
        System.out.print("masukan nama penerbit: ");
        penerbit = terminalinput.nextLine();
        System.out.print("masukan tahun diterbitkan format(YYYY): ");
        tahun = terminalinput.nextLine();

        boolean tahunvalid = false;
        while (!tahunvalid) {
            if (tahun.length() > 4){
                System.out.println("salah input tahun! format(YYYY)");
                System.out.print("masukan tahun diterbitkan: ");
                tahun = terminalinput.nextLine();
            }else{
                tahunvalid = true;
            }
        }
        //System.out.println(penulis + judul + penerbit + tahun);

        String[] keywords = {tahun + "," + penulis + "," + penerbit + "," + judul};
        System.out.println(Arrays.toString(keywords));

        boolean cek = utility.BukuAdaatauTidak(keywords,false);

        if (cek){ //jika data belum ada maka akan false{
            //fiersabesari_2012_1,2012,fiersa besari,media kita,jejak langkah
            String penuliswithoutspace = penulis.replaceAll("\\s+", "");
            long nomorentry = 1;
            String primarykey = penuliswithoutspace + "_" + tahun + "_" + nomorentry;
            System.out.println("primary key  : " + primarykey);
            System.out.println("tahun terbit : " + tahun);
            System.out.println("penulis      : " + penulis);
            System.out.println("penebit      : " + penerbit);
            System.out.println("judul buku   : " + judul);

            boolean lanjutTambah = utility.getYesorNo("anda ingin memasukan data ini atau tidak? (y/n)");

            String data = buffread.readLine();
            if (lanjutTambah){
                if ( data != null ){
                    buffwrite.newLine();
                }
                buffwrite.write(primarykey);
                buffwrite.write("," + tahun);
                buffwrite.write("," + penulis);
                buffwrite.write("," + penerbit);
                buffwrite.write("," + judul);
            }
        }
        buffwrite.flush();
        buffwrite.close();
        buffread.close();

        fileinput.close();
        fileoutput.close();

    }
    public static void tampilkanData() throws IOException{
        FileReader fileinput;
        BufferedReader buffread;

        try {
            fileinput = new FileReader("database.txt");
            buffread = new BufferedReader(fileinput);
        }catch (Exception ex){
            System.out.println("file tidak ditemukan");
            System.out.println("buatlah file terlebih dahulu");
            tambahdata();
            return;
        }

        String data;
        int i = 1;
        System.out.println("|   No |  Tahun | Penulis               |  Penerbit                |  Judul Buku");
        System.out.println("---------------------------------------------------------------------------------");


        while ( (data = buffread.readLine()) != null ) { //data tidak kosong
            if (!data.isEmpty()) {
                StringTokenizer fileToken = new StringTokenizer(data, ",");
                fileToken.nextToken();
                System.out.printf("| %3d  ", i);
                System.out.printf("|  %s  ", fileToken.nextToken());
                System.out.printf("| %-20s  ", fileToken.nextToken());
                System.out.printf("| %-25s", fileToken.nextToken());
                System.out.printf("| %s  ", fileToken.nextToken());
                System.out.println();
                i++;
            } else {
                continue;
            }
        }

        fileinput.close();
        buffread.close();

    }
    public static void cariData() throws IOException{

        // membaca database ada atau tidak
        try {
            File file = new File("database.txt");
        } catch (Exception ex){
            System.err.println("Database tidak ditemukan");
            System.err.println("Silahkan tambah database terlebih dahulu");
        }

        // mengambil keyword dari user

        Scanner terminalInput = new Scanner(System.in);
        System.out.print("masukan keeyword untuk mencari buku: ");
        String cariString = terminalInput.nextLine();

        String[] keywords = cariString.split("\\s+");

        utility.cekDataBukuDiDatabase(keywords);
    }
}
