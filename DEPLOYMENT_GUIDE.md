# Render Deployment Guide

## Prerequisites
- GitHub account with your repository
- Render account (free tier available)
- Node.js installed locally (for testing)

---

## Step-by-Step Deployment

### 1️⃣ Prepare Your Repository

Make sure all files are ready:
```bash
cd c:\Users\ADM\Desktop\kiprono-amon-portfolio

# Check what will be committed
git status

# Add all files
git add .

# Commit with message
git commit -m "Portfolio: production-ready with all content and images"
```

### 2️⃣ Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `kiprono-amon-portfolio`
3. Description: "Professional portfolio - Instructional Designer, Web Developer, Tech Leader"
4. Choose **Public** (for GitHub Pages option later)
5. Skip initialization (you already have local files)
6. Click "Create repository"

### 3️⃣ Push Code to GitHub

```bash
# From your local folder
git remote add origin https://github.com/kiprono10/kiprono-amon-portfolio.git
git branch -M main
git push -u origin main
```

**Verify:** Check github.com/kiprono10/kiprono-amon-portfolio - all files should appear

### 4️⃣ Deploy on Render.com

#### Option A: Manual Deploy (Recommended for First Time)

1. **Go to [render.com](https://render.com)**
   - Click "Sign up" or "Sign in"
   - Use GitHub to authenticate (easier)

2. **Create Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect GitHub account
   - Search for `kiprono-amon-portfolio`
   - Select and authorize

3. **Configure Service**
   - **Name:** `kiprono-amon-portfolio`
   - **Environment:** `Node`
   - **Build Command:** `npm install`
   - **Start Command:** `node server.js`
   - **Plan:** Free (sufficient for portfolio)

4. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically
   - Takes 2-5 minutes
   - You'll see live URL when ready

#### Option B: Auto-Deploy (Future Updates)

After first deployment:
- Any push to GitHub `main` branch = automatic Render deploy
- No manual action needed
- Takes ~1-2 minutes per update

---

## 📊 Expected Render Dashboard

After deployment, you'll see:
- **Status:** "Live" (green)
- **URL:** `https://kiprono-amon-portfolio.onrender.com`
- **Logs:** View build and runtime logs
- **Settings:** Manage environment, redeploy, restart

---

## ✅ Verify Deployment

1. **Check live URL**
   - Open: `https://kiprono-amon-portfolio.onrender.com`
   - Should see your full portfolio

2. **Test key features**
   - ✅ All sections visible
   - ✅ Images load correctly
   - ✅ Scroll animations work
   - ✅ Contact form opens
   - ✅ Links work (GitHub, LinkedIn, etc.)
   - ✅ Mobile responsive

3. **Test contact form**
   - Fill out form
   - Should receive email at `kipronoamon21@gmail.com`

---

## 🔧 Troubleshooting

### "Build Failed"
**Cause:** Missing dependencies or wrong build command

**Fix:**
```bash
# Verify locally
npm install
npm start
# Should run on http://localhost:5000
```

Then check:
- `package.json` exists
- `Procfile` has `web: node server.js`
- `.gitignore` excludes `node_modules`

### "Images Not Loading"
**Cause:** Incorrect image paths

**Current paths in HTML:**
```html
<img src="public/images/profile.jpg" alt="...">
<img src="public/images/resources/lmskemu.jfif" alt="...">
```

**Verify:**
- Images exist in `public/images/` folder
- Paths are relative (not absolute)
- Files are committed to GitHub

### "Port Already in Use"
**On Render:** Not an issue (Render manages ports)

**Locally:**
```bash
PORT=3000 npm start
# Opens on http://localhost:3000
```

### "Free Tier Spun Down"
**Render free tier:** May go to sleep after 15 min of inactivity

**Happens:** Browser will wait 15-30 sec on first visit
**Fix:** Upgrade to paid tier ($7/month) or just wait

---

## 📱 Custom Domain (Optional)

To use your own domain instead of `onrender.com`:

1. **On Render Dashboard**
   - Go to your service
   - Click "Settings"
   - Scroll to "Custom Domain"
   - Add your domain

2. **Update DNS Records**
   - Go to your domain registrar
   - Add Render's DNS records
   - Details provided by Render

3. **Wait for SSL**
   - Render auto-generates SSL certificate
   - Takes a few minutes

---

## 📋 File Checklist

Before deploying, verify these files exist:

```
✅ package.json (with "start": "node server.js")
✅ server.js (Express app)
✅ Procfile (web: node server.js)
✅ .gitignore (excludes node_modules)
✅ index.html (complete portfolio)
✅ script.js (JavaScript logic)
✅ public/images/ (all profile & project images)
✅ README.md (documentation)
```

---

## 🎉 After Deployment

### Share Your Portfolio
- **Twitter:** "Just launched my portfolio! 🚀 Check it out: [your-render-url]"
- **LinkedIn:** Add in profile
- **GitHub:** Add to projects
- **Resume:** Include live link

### Monitor Performance
- Render dashboard shows uptime
- Logs show any errors
- Check visitor activity

### Next Steps
- Get feedback from peers
- Update content as you complete new projects
- Consider adding blog section
- Implement backend admin system (Phase 2)

---

## 📞 Support

- **Render Docs:** render.com/docs
- **GitHub Help:** docs.github.com
- **Issues:** Check Render logs for error messages

---

**Status:** Ready for deployment! 🚀

**Last Updated:** February 2026
