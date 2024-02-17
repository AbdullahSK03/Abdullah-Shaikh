import Header from "../components/Header";
const Form = () => {
  return (
    <div>
      <Header />
      <div className="container contact-form mt-5">
        <h1>Contact Me</h1>
        <form action="">
          <div className="row ">
            <div className="col-md-6 col-sm-12">
              <input type="text" name="txtName" placeholder="Name" />
            </div>
            <div className="col-md-6 col-sm-12">
              <input type="phone" name="" placeholder="Phone Number" />
            </div>
          </div>
          <input type="text" id="email" name="txtEmail" placeholder="Email" />
          <textarea name="txtMsg" id="txtMsg" rows="10" placeholder="What's on your mind?"/>
          <button className="btnSubmit" >Sumbit</button>
        </form>
      </div>
    </div>
  );
};

export default Form;
