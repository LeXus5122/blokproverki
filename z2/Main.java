package z2;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        ToyStore store = new ToyStore();
        
        store.addToy("1", "конструктор", 2);
        store.addToy("2", "робот", 2);
        store.addToy("3", "кукла", 6);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("./output.txt"))) {
            for (int i = 0; i < 10; i++) {
                String toyId = store.getToyId();
                writer.write(toyId);
                writer.newLine();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

