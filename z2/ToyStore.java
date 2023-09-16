package z2;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Random;

public class ToyStore {
    private PriorityQueue<Toy> toysQueue = new PriorityQueue<>(
            (toy1, toy2) -> Integer.compare(toy2.getWeight(), toy1.getWeight())); // Самые тяжелые игрушки в начале
    private Random random = new Random();
    private List<Toy> allToys = new ArrayList<>();

    public void addToy(String id, String name, int weight) {
        Toy toy = new Toy(id, name, weight);
        for (int i = 0; i < weight; i++) {
            toysQueue.add(toy);
            allToys.add(toy);
        }
    }

    public String getToyId() {
        if (allToys.isEmpty()) {
            return null;
        }
        
        Toy selectedToy = allToys.get(random.nextInt(allToys.size()));
        allToys.remove(selectedToy);
        return selectedToy.getId();
    }
}
