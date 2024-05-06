package ssvv.lab1;

import domain.Nota;
import domain.Student;
import domain.Tema;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.junit.jupiter.api.Assertions;
import repository.NotaXMLRepo;
import repository.StudentXMLRepo;
import repository.TemaXMLRepo;
import service.Service;
import validation.NotaValidator;
import validation.StudentValidator;
import validation.TemaValidator;
import validation.ValidationException;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.assertThrows;

public class AppTestIntegration extends TestCase {

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

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTestIntegration( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTestIntegration.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
        assertTrue( true );
    }

    public void testAddStudentGoodEmailIntegration(){
        Student studentGoodEmail = new Student("1004", "Andrei", 933, "maria@email.com");

        Assertions.assertNull(service.addStudent(studentGoodEmail));
    }

    public void testAddGoodAssignmentIntegration(){
        Tema temaGoodAssignment = new Tema("125", "descriere", 12, 12);

        Assertions.assertNull(service.addTema(temaGoodAssignment));
    }

    public void testAddGradeWrongStudentIntegration(){
        LocalDate date = LocalDate.of(2018, 1, 12);
        Nota nota = new Nota("1", "1011", "2", 10, date);

        assertThrows(ValidationException.class, () -> {
            service.addNota(nota, "feedback");
        });
    }

    public void testAddGoodGradeIntegration(){

        Student studentGoodEmail = new Student("234", "Andrei", 933, "maria@email.com");
        service.addStudent(studentGoodEmail);

        Tema temaGoodAssignment = new Tema("127", "descriere", 12, 12);
        service.addTema(temaGoodAssignment);

        LocalDate date = LocalDate.of(2024, 4, 15);
        Nota nota = new Nota("15", studentGoodEmail.getID(), temaGoodAssignment.getID(), 5, date);

        Assertions.assertEquals(service.addNota(nota, "feedback"), 5.0);
    }


    // Homework tests
    public void testAddStudent(){
        Student student = new Student("1000", "Andrei", 933, "andrei@email.com");

        Assertions.assertNull(service.addStudent(student));
    }

    public void testAddStudentAndAddAssignment(){
        Student student = new Student("123123", "Maria", 933, "maria@email.com");
        Assertions.assertNull(service.addStudent(student));

        Tema tema = new Tema("12321", "descriere", 11, 11);
        Assertions.assertNull(service.addTema(tema));
    }

    public void testAddStudentAndAddAssignmentAndAddGrade(){
        Student student = new Student("12313", "Dorel", 933, "dorel@email.com");
        Assertions.assertNull(service.addStudent(student));

        Tema tema = new Tema("12311", "descriere", 11, 11);
        Assertions.assertNull(service.addTema(tema));

        LocalDate date = LocalDate.of(2024, 4, 15);
        Nota nota = new Nota("124312", student.getID(), tema.getID(), 10, date);

        Assertions.assertEquals(service.addNota(nota, "feedback"), 10.0);
    }
}
