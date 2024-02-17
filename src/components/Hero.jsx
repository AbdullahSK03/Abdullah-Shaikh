import React from "react";

const Hero = () => {
  return (
    <div className="px-4 py-5 my-5 text-center">
      <img
        src="src/assets/Abdullah Shaikh.jpg"
        alt=""
        className="pfp puff-in-center"
      />
      <h1 className="display-1 my-3 fw-bold text-body-emphasis text-focus-in">
        Abdullah Shiakh
      </h1>
      <hr />
      <p class="display-6 mx-auto text-body-emphasis text-focus-in">
        Student of Computer Science Engineering specialized in Artificial
        Intelligence and Machine Learning.
      </p>
      <p className="display-7 my-1 text-body-emphasis text-focus-in">And</p>
      <h1 className="display-6 text-body-emphasis text-focus-in">
        Full Stack Web Developer
      </h1>
    </div>
  );
};
export default Hero;
