import Header from "../components/Header";
import Cards from "../components/Cards";

const Qualification = () => {
  const certificates = [
    {
      id: 1,
      title: "Python Programming",
      desc: "Fluent with libraries like pandas, numpy, matplotlib, etc., Learning Tensorflow, PyTorch, ROCm, Cuda, etc.",
      imgSrc: "src/assets/python.webp",
      link: "https://1drv.ms/i/s!As5SftZQcsRNgatoqfqmzoJA8LmyJA?e=056dI3",
    },
    {
      id: 2,
      title: "IoT Board Programming",
      desc: "Beginner IoT board programmer",
      imgSrc: "src/assets/IoT.webp",
      link: "https://1drv.ms/i/s!As5SftZQcsRNgatnOyc1m-n-8lBoSA?e=WHRXQY",
    },
    {
      id: 3,
      title: "Web Development",
      desc: "Full Stack Web Developer speacialized in MERN Stack. Also have experience with Bootstrap, Tailwind, Flask, Jinja, etc.",
      imgSrc: "src/assets/WebDev.webp",
      link: "https://1drv.ms/i/s!As5SftZQcsRNgatoqfqmzoJA8LmyJA?e=qf7dz6",
    },
    {
      id: 4,
      title: "Advanced C++",
      desc: "Certified in advanced C++ programming with data structures and algorithms.",
      imgSrc: "src/assets/C++.webp",
      link: "https://1drv.ms/i/s!As5SftZQcsRNgatnOyc1m-n-8lBoSA?e=WHRXQY",
    },
  ];
  console.log(certificates);
  return (
    <div>
      <Header />
      <div className="container mt-5">
        <div className="row">
          {certificates.map((certificate) => (
            <div className="col-lg-3 col-md-6  col-sm-12 cardDisplay">
              <Cards cardInput={certificate} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Qualification;
