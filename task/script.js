const pages = {
    home: `<h2><i class="fas fa-home"></i> Home</h2>
    <p>Welcome to our homepage! Explore our content and discover more.</p>
    <div class="home-content">
        <h3>About Us</h3>
        <p>This is my original home page content...</p>
        <img src="https://th.bing.com/th/id/OIP.-VrhW9eiG8ugOKzvCy_jdwHaFw?rs=1&pid=ImgDetMain" alt="Home Image">
    </div>`,

    services: `<h2><i class="fas fa-cogs"></i> Services</h2>
               <p>We offer a wide range of services tailored to meet your needs. Whether you are looking for professional consultations, 
               digital solutions, or customer support, we have got you covered.</p>
               <ul>
                   <li><i class="fas fa-code"></i> <strong>Web Development:</strong> Creating user-friendly and responsive websites.</li>
                   <li><i class="fas fa-chart-line"></i> <strong>SEO Optimization:</strong> Enhancing your online presence with effective strategies.</li>
                   <li><i class="fas fa-headset"></i> <strong>Technical Support:</strong> 24/7 assistance to ensure smooth operations.</li>
               </ul>
               <p>Our team of experts is always here to assist you in achieving your goals with top-notch solutions.</p>`,

    contact: `<h2><i class="fas fa-envelope"></i> Contact</h2>
              <p>We would love to hear from you! Reach out to us through any of the following channels:</p>
              <ul>
                  <li><i class="fas fa-envelope"></i> <strong>Email:</strong> support@example.com</li>
                  <li><i class="fas fa-phone"></i> <strong>Phone:</strong> +123 456 7890</li>
                  <li><i class="fas fa-map-marker-alt"></i> <strong>Office Address:</strong> 123 Main Street, City, Country</li>
              </ul>
              <p>Feel free to drop us a message, and we will get back to you as soon as possible. Your feedback and inquiries are valuable to us!</p>`
};

function loadPage(page) {
    document.getElementById('content').innerHTML = pages[page] || '<h2>Page not found</h2>';
}
