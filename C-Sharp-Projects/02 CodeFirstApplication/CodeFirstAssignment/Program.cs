using System.Data.Entity;

namespace CodeFirstAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var db = new SchoolContext())
            {
                // ask user to enter name into database
                Console.Write("Hello, new student! Please enter your name into the database: ");
                var studentName = Console.ReadLine(); // name is set to var studentName

                var student = new Student { StudentName = studentName }; // instantiate a new Student, where StudentName will become var studentName
                db.Students.Add(student); // add to database
                db.SaveChanges(); // save changes

                // query logic to find students in the database
                var query = from s in db.Students
                            orderby s.StudentName
                            select s;

                // print query using foreach
                Console.WriteLine("\nHere is a list of students:");
                foreach (var item in query)
                {
                    Console.WriteLine(item.StudentName);
                }

                Console.WriteLine("\nSee you next time!");
                Console.ReadLine();
            }
        }
    }
}
public class SchoolContext : DbContext
{
    public SchoolContext() : base()
    {
    }
    public DbSet<Student> Students { get; set; }
    public DbSet<Grade> Grades { get; set; }
}
public class Student
{
    public int StudentID { get; set; }
    public string StudentName { get; set; }
    public Grade Grade { get; set; }
}

    public class Grade
{
    public int GradeId { get; set; }
    public string GradeName { get; set; }
    public string Section { get; set; }

    public ICollection<Student> Students { get; set; }
}