# 包装建厂选址模拟器 - Flask Web 部署版（适配 Render）

本项目是一个用于投资评估与城市选址决策的交互式模拟器，支持：

✅ 城市ROI与利润分析  
✅ 权重评分计算与推荐排序  
✅ 图表可视化（柱状图）  
✅ 在线部署到 Render.com

---

## 🚀 一键部署到 Render 云平台

### 第一步：上传到你的 GitHub 仓库

1. 登录 GitHub
2. 创建新仓库（推荐命名：`factory-site-selector`）
3. 上传本项目所有文件（解压后拖入即可）

---

### 第二步：登录 Render 并创建 Web Service

1. 打开 https://render.com
2. 点击“New +” → Web Service
3. 连接 GitHub，选择你上传的仓库

#### 配置如下：

- **Environment**: Python 3
- **Start command**:
  ```
  python app.py
  ```
- **Build command**: 空即可（默认）
- **Port**: 默认 10000 或自动识别

---

### 第三步：访问你的网站！

部署完成后 Render 会分配一个地址，比如：
```
https://your-simulator-name.onrender.com/
```

---

## 📦 本项目结构说明

| 文件/目录         | 说明                       |
|------------------|----------------------------|
| `app.py`         | Flask主程序入口             |
| `templates/`     | HTML前端页面模板             |
| `modules/`       | 后端数据分析模块（含图表生成） |
| `requirements.txt` | Flask + matplotlib依赖      |
| `Procfile`       | Render部署专用启动文件       |
| `runtime.txt`    | 指定Python版本（3.9）        |

---

有任何问题欢迎联系你的技术支持人员或部署协助。
