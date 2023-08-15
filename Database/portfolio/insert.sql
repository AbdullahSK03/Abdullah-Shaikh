
INSERT INTO certificate(course, C_Desc, img)
VALUES
('Internet Of Things', 'Worked and Studied with IoT boards as a field of interest', 
    (SELECT * FROM OPENROWSET(BULK 'F:\Learning\Abdullah-Shaikh\Database\portfolio\Certificates\Untitled.webp', SINGLE_BLOB) as ImageData)
),
('Web Developer', 'I am a certified web developer with good understanding of HTML5, CSS3, JavaScript also learning NodeJs also have experience with Flask and Jinja templating',
    (SELECT * FROM OPENROWSET(BULK 'F:\Learning\Abdullah-Shaikh\Database\portfolio\Certificates\WebDev.webp', SINGLE_BLOB) as ImageData)
),
('Advance C++', 'Advance C++ is also a field in which I have excelled. I also have deep understanding of how OOP work with C++ and also have deep knowledge about implementing data structures using C/C++',
    (SELECT * FROM OPENROWSET(BULK 'F:\Learning\Abdullah-Shaikh\Database\portfolio\Certificates\C++.webp', SINGLE_BLOB) as ImageData)
),
('Python', 'Python Programming language is one of programimng language which I have excellent command on. I have also worked with libraries Tkinter, Pandas, Flask, openCV, etc.', 
	(SELECT * FROM OPENROWSET(BULK 'F:\Learning\Abdullah-Shaikh\Database\portfolio\Certificates\PYTHON.WEBP', SINGLE_BLOB) AS IMAGE)
)


SELECT * FROM certificate