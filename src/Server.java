import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.SimpleDateFormat;  
import java.util.Date;
import java.sql.Timestamp;
public class Server {
    public static void main(String[] args) throws IOException {
        int c = 0;
        while (true) {
            ServerSocket serverSocket = null;
            try {
                serverSocket = new ServerSocket(4444);
            } catch (IOException ex) {
                System.out.println("Can't setup server on this port number. ");
            }
            Socket socket = null;
            InputStream in = null;
            OutputStream out = null;

            try {
                socket = serverSocket.accept();
            } catch (IOException ex) {
                System.out.println("Can't accept client connection. ");
            }

            try {
                in = socket.getInputStream();
            } catch (IOException ex) {
                System.out.println("Can't get socket input stream. ");
            }

            try {
				//SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
				//Date date = new Date();
			    
				Date date=java.util.Calendar.getInstance().getTime(); 
		
                out = new FileOutputStream("E:\\Project\\CameraPhotos\\data"+random()+".jpg");
                c++;
            } catch (FileNotFoundException ex) {
                System.out.println("File not found. ");
            }

            byte[] bytes = new byte[16000*1024];

            int count = 0;
            while ((count = in.read(bytes)) > 0)
             {
                 out.write(bytes, 0, count);
             }

            out.close();
            in.close();
            socket.close();
            serverSocket.close();

            System.out.println(c+" file found ");
        }

    }
	
	static String random()
	{
			SimpleDateFormat sdf = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss");
			return sdf.format(new Date().getTime());
			
	}
	
	
}