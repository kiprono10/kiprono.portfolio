# 🚀 Deploy to Render - Quick Commands

Copy and paste these commands in order. Takes ~10 minutes total.

---

## 1️⃣ Prepare Your Local Folder

```bash
cd c:\Users\ADM\Desktop\kiprono-amon-portfolio
```

---

## 2️⃣ Initialize Git (One Time)

```bash
git init
git add .
git commit -m "Portfolio: production-ready with Render deployment config"
```

---

## 3️⃣ Create GitHub Repository

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name:** `kiprono-amon-portfolio`
   - **Description:** Professional portfolio - Instructional Designer, Web Developer, Tech Leader
   - **Public:** Yes
3. Click **Create repository**
4. Copy the HTTPS URL (looks like: `https://github.com/kiprono10/kiprono-amon-portfolio.git`)

---

## 4️⃣ Push Code to GitHub

Replace `YOUR_REPO_URL` with the URL from step 3:

```bash
git remote add origin YOUR_REPO_URL
git branch -M main
git push -u origin main
```

**Example:**
```bash
git remote add origin https://github.com/kiprono10/kiprono-amon-portfolio.git
git branch -M main
git push -u origin main
```

---

## 5️⃣ Deploy on Render

### A. Create Account
1. Go to: https://render.com
2. Sign up / Log in with GitHub

### B. Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Click **"Connect account"** to GitHub
3. Authorize Render access
4. Find and select `kiprono-amon-portfolio`
5. Click **"Connect"**

### C. Configure Settings

| Setting | Value |
|---------|-------|
| **Name** | `kiprono-amon-portfolio` |
| **Environment** | `Node` |
| **Build Command** | `npm install` |
| **Start Command** | `node server.js` |
| **Plan** | Free |

6. Click **"Create Web Service"**
7. Wait 2-5 minutes for deployment ⏳

---

## ✅ Verify Deployment

### Check Status
1. Go to your Render dashboard
2. Should see green "Live" status
3. Your URL: `https://kiprono-amon-portfolio.onrender.com`

### Test the Site
1. Open the URL in browser
2. Check all sections load
3. Test contact form (send yourself an email)
4. Test all links work

---

## 🎉 You're Live!

Your portfolio is now on the internet at:
```
https://kiprono-amon-portfolio.onrender.com
```

### Share It!
- **LinkedIn:** Add to profile
- **Twitter:** "Just launched my portfolio! 🚀"
- **Resume:** Include the link
- **GitHub:** Add to profile README

---

## ⚠️ Common Issues

### "Build Failed"
```bash
# Test locally first
npm install
npm start
# Visit http://localhost:5000
```

### "Images Not Loading"
- Verify files in `public/images/` folder
- Check they're committed to GitHub
- Restart Render service (Settings → Restart)

### "Free Tier - Service Spinning Down"
- Render free tier sleeps after 15 min inactivity
- First visit takes ~30 seconds (normal!)
- Upgrade to Starter Plan ($7/month) for always-on

---

## 📞 Support

- **Render Docs:** https://render.com/docs
- **GitHub Issues:** Check repo settings
- **Emergency:** Restart service in Render dashboard

---

**Ready? Let's deploy! 🚀**
