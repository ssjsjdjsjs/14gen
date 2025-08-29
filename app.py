import express from 'express';
import fetch from 'node-fetch'; // Vercel ortamında fetch global olabilir, gerekirse kaldır

const app = express();

app.get('/myField14', async (req, res) => {
  const { open_id } = req.query; // open_id sorgudan alınır

  if (!open_id) {
    return res.status(400).json({ error: "open_id eksik" });
  }

  try {
    const response = await fetch(`https://ffbd-v2.vercel.app/field14_bySamiul?open_id=${open_id}`);
    const data = await response.json();

    // Sadece field_14'ü döndür
    res.json({ field_14: data.field_14 });
  } catch (err) {
    res.status(500).json({ error: "API isteği başarısız" });
  }
});

export default app;
