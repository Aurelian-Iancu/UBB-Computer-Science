import domain.Student;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import repository.CrudRepository;
import repository.NotaXMLRepo;
import repository.StudentXMLRepo;
import repository.TemaXMLRepo;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;
import view.UI;

import static org.junit.jupiter.api.Assertions.assertThrows;

public class TestAddStudent {
    @Test
    public void testAddStudent(){
        StudentValidator studentValidator = new StudentValidator();
        TemaValidator temaValidator = new TemaValidator();
        String filenameStudent = "fisiere/Studenti.xml";
        String filenameTema = "fisiere/Teme.xml";
        String filenameNota = "fisiere/Note.xml";

        StudentXMLRepo studentXMLRepository = new StudentXMLRepo(filenameStudent);
        TemaXMLRepo temaXMLRepository = new TemaXMLRepo(filenameTema);
        NotaValidator notaValidator = new NotaValidator(studentXMLRepository, temaXMLRepository);
        NotaXMLRepo notaXMLRepository = new NotaXMLRepo(filenameNota);
        Service service = new Service(studentXMLRepository, studentValidator, temaXMLRepository, temaValidator, notaXMLRepository, notaValidator);

        // invalid student
        Student student1 = new Student("", "ana", 933, "ana@email.com");

        assertThrows(ValidationException.class, () -> {
            service.addStudent(student1);
        });

        // valid student
        Student student2 = new Student("12", "maria", 933, "maria@email.com");

        Assertions.assertNull(service.addStudent(student2));

    }
}
