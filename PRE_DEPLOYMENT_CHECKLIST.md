# Pre-Deployment Checklist ✅

## Before Pushing to GitHub

### Code Quality
- [ ] `npm install` runs without errors
- [ ] `npm start` runs on http://localhost:5000
- [ ] All pages load correctly
- [ ] No console errors in browser DevTools
- [ ] All images display (check public/images folder)
- [ ] All links work (GitHub, LinkedIn, etc.)

### Files Present
- [ ] `index.html` - Portfolio page (866 lines)
- [ ] `script.js` - Frontend logic (92 lines)
- [ ] `server.js` - Express app
- [ ] `package.json` - Dependencies with "start" script
- [ ] `Procfile` - Contains: `web: node server.js`
- [ ] `.gitignore` - Excludes node_modules, .env, etc.
- [ ] `public/images/` folder with all images

### Content Verification
- [ ] Hero section displays correctly
- [ ] All 9 portfolio sections visible
- [ ] Contact form is functional
- [ ] All 6 projects show images
- [ ] Social links are correct
- [ ] Email contact is correct: kipronoamon21@gmail.com
- [ ] Phone number is correct: +254 746 426 773

### Images
- [ ] `profile.jpg` in public/images/
- [ ] `profile-alt2.jpg` in public/images/
- [ ] All 6 project images in `public/images/resources/`:
  - [ ] `lmskemu.jfif`
  - [ ] `ukulimabora.jfif`
  - [ ] `trashtrack.jfif`
  - [ ] `powervision.jfif`
  - [ ] `greenhorizon.jfif`
  - [ ] `edutech.jpg`

---

## GitHub Setup

- [ ] GitHub account exists
- [ ] Created repository: `kiprono-amon-portfolio`
- [ ] Repository is public
- [ ] Code pushed to main branch

### Push Command
```bash
git init
git add .
git commit -m "Initial portfolio commit"
git remote add origin https://github.com/kiprono10/kiprono-amon-portfolio.git
git branch -M main
git push -u origin main
```

---

## Render Deployment

- [ ] Render account created (free)
- [ ] Logged in with GitHub
- [ ] Created Web Service
- [ ] Connected to `kiprono-amon-portfolio` repo

### Settings on Render
- [ ] **Environment:** Node
- [ ] **Build Command:** `npm install`
- [ ] **Start Command:** `node server.js`
- [ ] **Plan:** Free tier selected

### After Deploy
- [ ] Service shows "Live" status
- [ ] Can open live URL
- [ ] Portfolio displays fully
- [ ] Contact form test sent (check email)
- [ ] All links work on live site

---

## Testing Live Portfolio

### Desktop (Chrome/Firefox/Safari)
- [ ] Page loads in under 3 seconds
- [ ] All sections visible and styled correctly
- [ ] Scroll animations work (AOS.js)
- [ ] Contact form submits successfully
- [ ] All images load without errors
- [ ] Links open in new tabs where applicable

### Mobile (On Phone or DevTools)
- [ ] Layout is responsive
- [ ] Navigation menu works (hamburger menu)
- [ ] Images scale properly
- [ ] Form is usable
- [ ] No text overlap
- [ ] Touch interactions smooth

### Forms & Links
- [ ] Fill contact form → "Success" message
- [ ] Check email for form submission
- [ ] Click GitHub link → github.com/kiprono10
- [ ] Click LinkedIn → correct profile
- [ ] Click Twitter → @AmonKiprono12
- [ ] Click Instagram → k.i.p.ro.n.o
- [ ] Project "View Code" links work
- [ ] Project demo links work (if any)

---

## Performance Check (Optional)

### Page Speed
- [ ] Lighthouse score > 80 (Google DevTools)
- [ ] First Contentful Paint < 2 seconds
- [ ] Largest Contentful Paint < 3 seconds
- [ ] Images optimized (under 5MB total)

### Browser Compatibility
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

---

## Troubleshooting Checkpoints

If something doesn't work:

1. **Build Failed on Render?**
   - [ ] Check Render logs for error message
   - [ ] Verify `npm install` works locally
   - [ ] Ensure all dependencies in package.json

2. **Images Not Loading?**
   - [ ] Check file paths in HTML match actual files
   - [ ] Verify images committed to GitHub
   - [ ] Check Render build logs for errors

3. **Form Not Submitting?**
   - [ ] FormSubmit.co endpoint is public
   - [ ] Email address is correct in form action
   - [ ] No browser console errors

4. **Site Very Slow?**
   - [ ] Free tier Render may sleep → wait 30 seconds
   - [ ] Upgrade to paid if consistent issues
   - [ ] Check browser cache (Ctrl+Shift+Del)

---

## Post-Launch

- [ ] Share URL on LinkedIn/Twitter
- [ ] Add to GitHub profile README
- [ ] Add to resume
- [ ] Monitor Render dashboard for issues
- [ ] Keep GitHub repo updated with new projects

---

**Portfolio Status:** Ready for deployment! 🚀
**Last Checked:** February 2026
