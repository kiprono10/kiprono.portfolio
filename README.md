# Too Amon Kiprono - Professional Portfolio

A modern, responsive portfolio website showcasing instructional design, web development, and tech community leadership.

**Status:** ✅ Production Ready | 🚀 Deploying to Render

## 🎯 Overview

This portfolio is designed to attract **remote opportunities**, **freelance clients**, and **tech roles**. It presents a professional, clean aesthetic with smooth interactivity and modern UX principles.

---

## 🚀 Quick Deploy to Render

### Step 1: Push to GitHub
```bash
cd kiprono-amon-portfolio
git init
git add .
git commit -m "Initial portfolio commit"
git remote add origin https://github.com/kiprono10/kiprono-amon-portfolio.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Create new Web Service from GitHub repo
3. Set **Start Command:** `node server.js`
4. Set **Build Command:** `npm install`
5. Click "Create Web Service" 🎉

**Your portfolio will be live at:** `https://kiprono-amon-portfolio.onrender.com`

---

## 📁 Project Structure

```
kiprono-amon-portfolio/
├── index.html              # Main portfolio (866 lines, production-ready)
├── script.js               # Frontend interactivity (92 lines)
├── styles.css              # Custom styles
├── server.js               # Express server (Node.js backend)
├── package.json            # Dependencies
├── Procfile                # Render deployment config
├── .gitignore              # Git exclusions
├── README.md               # This file
└── public/                 # Static assets
    └── images/
        ├── profile.jpg                 # About section
        ├── profile-alt2.jpg            # Hero section
        └── resources/
            ├── lmskemu.jfif            # LMS Project
            ├── ukulimabora.jfif        # Agriculture
            ├── trashtrack.jfif         # Waste Management
            ├── powervision.jfif        # Energy
            ├── greenhorizon.jfif       # Sustainability
            └── edutech.jpg             # Digital Learning
```

---

## 🎨 Design System

### Color Palette
- **Primary:** `#0F172A` (Deep Slate)
- **Accent:** `#22C55E` (Emerald Green)
- **Secondary:** `#38BDF8` (Sky Blue)
- **Background:** `#020617` (Dark Blue-Black)
- **Card BG:** `#0B1220`
- **Text Primary:** `#E5E7EB` (Light Gray)
- **Text Muted:** `#94A3B8` (Slate Gray)

### Typography
- **Headings:** Poppins / Inter
- **Body:** Inter
- **Font Scale:** H1: 5xl | H2: 4xl | H3: 3xl | Body: base

---

## 🚀 Features

### Frontend (Live)
- ✅ Responsive navbar (sticky + blur effect)
- ✅ Hero section with typing animation
- ✅ About Me section
- ✅ Skills grid (6 categories)
- ✅ Featured Projects (6 projects with tech tags)
- ✅ Professional Experience timeline
- ✅ Certifications & Leadership
- ✅ Contact form
- ✅ Social media links
- ✅ AOS (Animate On Scroll) transitions
- ✅ Mobile menu (hamburger)
- ✅ Smooth scrolling

### Backend (To Be Built)
- Admin login with session authentication
- CRUD operations for:
  - About content
  - Skills
  - Projects
  - Experience
  - Certifications
- Image upload functionality
- MongoDB database integration

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (Tailwind CSS CDN)
- JavaScript (Vanilla)
- AOS.js (Scroll Animations)

### Backend (Ready for Development)
- Node.js
- Express.js
- MongoDB
- Bcryptjs (Password hashing)
- JWT (Authentication)

---

## 📋 Sections Breakdown

### 1. Navbar
- Sticky positioning
- Smooth blur backdrop
- Mobile hamburger menu
- Active link highlighting on scroll

### 2. Hero Section
- Full-screen height
- Typing animation for roles
- Call-to-action buttons
- Social media icons
- Scroll indicator

### 3. About
- Professional summary
- 4 quick fact cards (Mission, Focus, Experience, Values)
- Grid layout with animations

### 4. Skills
- 6 skill categories:
  - Web Development
  - Instructional Design
  - Design & Graphics
  - Tools & Platforms
  - IT Support & Networking
  - Soft Skills
- Interactive skill badges

### 5. Projects
- 6 featured projects
- Project cards with:
  - Emoji placeholder images
  - Description
  - Tech stack tags
  - Action buttons (Case Study, GitHub, Live Demo)
- Hover animations (card lift + image zoom)

### 6. Experience
- 4 professional roles
- Timeline format
- Job responsibilities as bullet points
- Alternating left/right layout

### 7. Certifications & Leadership
- Certifications (4 items)
- Leadership & Community (4 items)
- Two-column grid

### 8. Contact
- Contact form (Name, Email, Subject, Message)
- Success message
- Direct contact info (Email, Phone)
- Social media links

### 9. Footer
- Copyright info
- Links (Privacy, Terms, Contact)

---

## 🎬 Getting Started

### View the Portfolio

1. **Open in browser:**
   ```bash
   # Simply open index.html in your browser
   # Or use Live Server in VS Code
   ```

2. **No backend required yet** - the frontend is fully functional and static.

---

## 📝 Customization

### Edit Portfolio Content

1. **Name/Title:** Find `<h1>Too Amon Kiprono</h1>` in the hero section
2. **About Text:** Modify the `<p>` tags in the About section
3. **Skills:** Edit the skill categories and badges in the Skills section
4. **Projects:** Update project cards with your work
5. **Experience:** Change job titles, companies, dates
6. **Certifications:** Update your actual certifications
7. **Contact Info:** Update email and phone numbers

### Modify Colors

Edit the Tailwind config in the `<script>` tag within `<head>`:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                'emerald': '#YOUR_COLOR',
                'sky': '#YOUR_COLOR'
            }
        }
    }
}
```

### Add Your Own Images

Replace emoji placeholders with real project images:

```html
<!-- Replace this: -->
<span class="text-6xl">📚</span>

<!-- With this: -->
<img src="/images/project1.jpg" alt="Project Title">
```

---

## 🔐 Backend Setup (Next Phase)

### Coming Soon:
- Admin authentication system
- Database integration
- CRUD API endpoints
- Image upload system

### Planned Endpoints:
```
POST   /api/auth/login
POST   /api/auth/logout
POST   /api/projects
GET    /api/projects
PUT    /api/projects/:id
DELETE /api/projects/:id
[Similar for skills, experience, etc.]
```

---

## 📱 Responsiveness

The portfolio is fully responsive:
- ✅ Mobile (320px - 767px)
- ✅ Tablet (768px - 1024px)
- ✅ Desktop (1025px+)

Breakpoints: `md:` (768px), `lg:` (1024px)

---

## ⚡ Performance Optimizations

- Tailwind CSS for minimal CSS
- AOS for efficient scroll animations
- Lazy loading ready
- No heavy dependencies

---

## 🔗 Links to Update

Update these before deploying:
- Social links (LinkedIn, GitHub, Twitter)
- Email address
- Phone number
- CV download link

---

## 📞 Contact & Support

For questions or suggestions about the portfolio setup, refer to the contact form or reach out directly.

---

## 📜 License

MIT License - Feel free to customize and use this portfolio.

---

**Built with:** HTML, Tailwind CSS, Vanilla JavaScript, AOS
**Date:** February 2026
**Author:** Too Amon Kiprono
