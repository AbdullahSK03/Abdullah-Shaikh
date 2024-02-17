import { useLocation } from "react-router";

const Header = () => {
  const location = useLocation();
  let brandName;

  if (location.pathname !== "/") {
    brandName = location.pathname.slice(1);
  } else {
    brandName = location.pathname.slice(1);
  }

  return (
    <div className="container-fluid Nav-bar">
      <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
          <a class="navbar-brand" href="/">
            <img src="src/assets/Logo.jpg" className="logo" alt="" />
            {brandName}
          </a>
          {/* <a href="/" class="navbar-brand">Abdullah Shaikh</a> */}
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarText"
            aria-controls="navbarText"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarText">
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item align-middle">
                <a class="nav-link active" aria-current="page" href="/">
                  Home
                </a>
              </li>
              <li class="nav-item align-middle">
                <a class="nav-link active" href="Qualification">
                  Qualification
                </a>
              </li>
              <li class="nav-item align-middle">
                <a class="nav-link active" href="Contact">
                  Contact Me
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
};

export default Header;
