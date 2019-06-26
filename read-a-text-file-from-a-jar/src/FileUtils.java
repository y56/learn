import java.io.*;
import java.util.*;

public class FileUtils{

    public static List<String> readTextFromJar(String s) {
        InputStream is = null;
        BufferedReader br = null;
        String line;
        ArrayList<String> list = new ArrayList<String>();

        try {
            is = FileUtils.class.getResourceAsStream(s);
            br = new BufferedReader(new InputStreamReader(is));
            while (null != (line = br.readLine())) {
                list.add(line);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            try {
                if (br != null) br.close();
                if (is != null) is.close();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
        return list;
    }

    public static void main(String args[]) throws IOException{
        List<String> list = FileUtils.readTextFromJar("/datafile1.txt");
        Iterator<String> it = list.iterator();
        System.out.println("1");
        while(it.hasNext()) {
            System.out.println(it.next());
        }

        list = FileUtils.readTextFromJar("/test/datafile2.txt");
        it = list.iterator();
        System.out.println("2");
        while(it.hasNext()) {
            System.out.println(it.next());
        }
    }
}