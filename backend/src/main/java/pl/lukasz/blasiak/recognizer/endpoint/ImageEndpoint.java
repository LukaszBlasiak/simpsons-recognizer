package pl.lukasz.blasiak.recognizer.endpoint;

import org.apache.commons.codec.binary.Base64;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import sun.misc.BASE64Decoder;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@RestController
public class ImageEndpoint {

    private Random rand = new Random();

    @PostMapping(value = "/api/image")
    public ResponseEntity<Integer> newImage(@RequestBody String imageAsBase64) {
        Integer requestId = createRecognizeRequest(imageAsBase64);
        return new ResponseEntity<>(requestId, HttpStatus.OK);
    }

    @GetMapping(value = "/api/image")
    public ResponseEntity<String> getImage(@RequestParam Integer id) {
        String imageAsBase64 = getRecognizedImage(id);
        if(imageAsBase64 == null){
            return new ResponseEntity<>(HttpStatus.NOT_FOUND);
        }
        return new ResponseEntity<>(imageAsBase64, HttpStatus.OK);
    }


    private String getRecognizedImage(Integer id){
        try (Stream<Path> walk = Files.walk(Paths.get("images_workspace/recognized"))) {

            List<String> result = walk.filter(Files::isRegularFile)
                    .map(Path::toString)
                    .filter(fileName->fileName.contains(id.toString()+"-recognized"))
                    .collect(Collectors.toList());

            result.forEach(System.out::println);
            if(!result.isEmpty()){
                return imageToBase64(result.get(0));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private String imageToBase64(String imagePath) throws Exception{
        File file =  new File(imagePath);
        FileInputStream fileInputStreamReader = new FileInputStream(file);
        byte[] bytes = new byte[(int)file.length()];
        fileInputStreamReader.read(bytes);
        String valueToReturn = new String(Base64.encodeBase64(bytes), StandardCharsets.UTF_8);
        fileInputStreamReader.close();
        return valueToReturn;
    }

    private Integer createRecognizeRequest(String imageAsBase64){
        BufferedImage image = null;
        byte[] imageByte;
        try {
            BASE64Decoder decoder = new BASE64Decoder();
            imageByte = decoder.decodeBuffer(imageAsBase64.split(",")[1]);
            ByteArrayInputStream bis = new ByteArrayInputStream(imageByte);
            image = ImageIO.read(bis);
            bis.close();
            Integer id = this.rand.nextInt() & Integer.MAX_VALUE;;
            File outputfile = new File("images_workspace/" + id.toString() + "-to_recognize.jpg");
            ImageIO.write(image, "jpg", outputfile);
            return id;
        } catch (Exception e) {
            e.printStackTrace();
            return -1;
        }
    }

}
