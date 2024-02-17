import { Link } from "react-router-dom";

const Cards = ({ cardInput }) => {
  return (
    <div class="card">
      <img src={cardInput.imgSrc} class="card-img-top" alt={cardInput.title} />
      <div class="card-body">
        <h5 class="card-title">{cardInput.title}</h5>
        <p class="card-text">{cardInput.desc}</p>
        <Link to={cardInput.link} class="btn btn-primary">View</Link>
      </div>
    </div>
  );
};

export default Cards;