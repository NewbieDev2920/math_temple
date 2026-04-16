# Math Temple

**Math Temple** is a beautifully designed, minimalist daily mathematics web application. Inspired by the strict elegance of classic mathematical textbooks, it serves up a new collection of carefully curated mathematics exercises every day at midnight.

## Features

- **Daily Exercises**: Delivers 4 daily randomized math challenges (Definition, Theorem, Proof, and Computation).
- **Mathematical Quotes**: Each day begins with a profound quote from a prominent mathematician or scientist.
- **Textbook Typography**: Powered by **MathJax** and **Computer Modern** fonts, rendering LaTeX seamlessly to mimic the aesthetic of real mathematics textbooks.
- **Beautiful Code Execution**: Uses **Prism.js** to display algorithmic computation exercises (like Python scripts) elegantly.
- **Markdown Support**: Uses **marked.js** to format logic, bold text, lists, and structure right out of JSON banks.
- **Dark Elegance**: Designed with **TailwindCSS** for a distraction-free, zero-clutter, dark-mode-first mathematical environment.

## Data Structure

The exercises are drawn from 5 different JSON banks located in the `src/data/` directory:
- `definitions.json`
- `theorems.json`
- `proofs.json`
- `computations.json`
- `quotes.json`

### Creating New Questions

You can expand the daily banks by adding new dictionary entries to these JSON files.

**Standard Question Format (`definitions.json`, `theorems.json`, `proofs.json`, `computations.json`):**
```json
{
  "question": "What is the definition of a limit of a sequence $(x_n)$?",
  "answer": "A sequence $(x_n)$ converges to a limit $L$ if ...",
  "image": "images/example.png" // (Optional attribute) Note: images go inside src/static/images/
}
```
*Note: Write LaTeX inline using `$...$` and display blocks using `$$...$$`.*

**Quote Format (`quotes.json`):**
```json
{
  "quote": "If I have seen further it is by standing on the shoulders of Giants.",
  "author": "Isaac Newton"
}
```

## Running the Project

Ensure you have activated your Python virtual environment.

1. **Install Requirements**
   The application fundamentally requires Flask. If you haven't installed it:
   ```bash
   pip install flask
   ```

2. **Run the Math Temple Server**
   Navigate to the `src` folder and start the Flask app:
   ```bash
   cd src
   python app.py
   ```

3. **Visit the Temple**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Architecture Notes

The application uses an in-memory caching system based on dates (`datetime.date.today()`). This cache allows questions to be randomly chosen exactly once per day with a uniform distribution—guaranteeing that the user sees the same problem set throughout the whole day without relying on external cron jobs or background database schedulers.
