```html
<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Form Studio & Code Generator</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        forest: '#123B32',
                        greenLab: '#19745E',
                        mintLab: '#DDEFE7',
                        creamLab: '#F6F7F1',
                        inkLab: '#1B352E'
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome Icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .glass { background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); }
        .dark .glass { background: rgba(18, 59, 50, 0.9); backdrop-filter: blur(10px); }
        input, select, textarea { transition: all 0.2s ease; }
    </style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 min-h-full flex flex-col font-sans transition-colors duration-300">

    <header class="sticky top-0 z-50 glass border-b border-slate-200 dark:border-slate-800 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="bg-emerald-600 text-white p-2 rounded-xl shadow-md">
                    <i class="fa-solid fa-file-lines text-lg"></i>
                </div>
                <div>
                    <h1 class="font-bold text-base tracking-tight leading-none">TextForm <span class="text-emerald-600 dark:text-emerald-400">Studio</span></h1>
                    <span class="text-xs text-slate-500 dark:text-slate-400">Builder, Live Preview & Code Generator</span>
                </div>
            </div>
            <div class="flex items-center space-x-3">
                <button onclick="switchTab('builder')" id="btnBuilder" class="px-3 py-1.5 rounded-lg text-sm font-medium bg-emerald-600 text-white shadow-sm transition">
                    <i class="fa-solid fa-wand-magic-sparkles mr-1.5"></i> Form Builder
                </button>
                <button onclick="switchTab('code')" id="btnCode" class="px-3 py-1.5 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition">
                    <i class="fa-solid fa-code mr-1.5"></i> Code & Export
                </button>
                <button onclick="toggleTheme()" class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 transition" title="Toggle Theme">
                    <i id="themeIcon" class="fa-solid fa-moon text-slate-600 dark:text-slate-300"></i>
                </button>
            </div>
        </div>
    </header>

    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        
        <!-- Tab 1: Form Builder & Live Preview -->
        <div id="tabBuilder" class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            
            <!-- Left Control Panel -->
            <div class="lg:col-span-5 space-y-6">
                <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 p-6">
                    <h2 class="text-lg font-bold mb-4 flex items-center gap-2 text-emerald-600 dark:text-emerald-400">
                        <i class="fa-solid fa-sliders"></i> Form Configuration
                    </h2>

                    <div class="space-y-4">
                        <div>
                            <label class="block text-sm font-medium mb-1">Form Title</label>
                            <input type="text" id="formTitleInput" value="Student Lab Submission" oninput="updatePreview()" class="w-full px-3 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                        </div>

                        <div>
                            <label class="block text-sm font-medium mb-1">Form Description / Subtitle</label>
                            <input type="text" id="formDescInput" value="Fill in your details and experiment data below." oninput="updatePreview()" class="w-full px-3 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                        </div>

                        <div class="grid grid-cols-2 gap-4">
                            <div>
                                <label class="block text-sm font-medium mb-1">Accent Theme</label>
                                <select id="formTheme" onchange="updatePreview()" class="w-full px-3 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                                    <option value="emerald">Emerald Forest</option>
                                    <option value="indigo">Indigo Corporate</option>
                                    <option value="amber">Amber Warmth</option>
                                </select>
                            </div>
                            <div>
                                <label class="block text-sm font-medium mb-1">Button Alignment</label>
                                <select id="buttonAlign" onchange="updatePreview()" class="w-full px-3 py-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                                    <option value="right">Right Aligned</option>
                                    <option value="left">Left Aligned</option>
                                    <option value="full">Full Width</option>
                                </select>
                            </div>
                        </div>

                        <div class="pt-2 border-t border-slate-200 dark:border-slate-800">
                            <label class="block text-sm font-medium mb-2">Form Fields Included:</label>
                            <div class="space-y-2 text-sm">
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" id="fieldStudentName" checked onchange="updatePreview()" class="rounded text-emerald-600 focus:ring-emerald-500 w-4 h-4">
                                    <span>Student Name</span>
                                </label>
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" id="fieldRollNo" checked onchange="updatePreview()" class="rounded text-emerald-600 focus:ring-emerald-500 w-4 h-4">
                                    <span>Roll Number / ID</span>
                                </label>
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" id="fieldSubject" checked onchange="updatePreview()" class="rounded text-emerald-600 focus:ring-emerald-500 w-4 h-4">
                                    <span>Subject / Category (Dropdown)</span>
                                </label>
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" id="fieldDate" checked onchange="updatePreview()" class="rounded text-emerald-600 focus:ring-emerald-500 w-4 h-4">
                                    <span>Submission Date</span>
                                </label>
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" id="fieldComments" checked onchange="updatePreview()" class="rounded text-emerald-600 focus:ring-emerald-500 w-4 h-4">
                                    <span>Comments / Notes (Textarea)</span>
                                </label>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 p-6">
                    <h3 class="font-bold text-md mb-2 flex items-center gap-2">
                        <i class="fa-solid fa-lightbulb text-amber-500"></i> Quick Copy Options
                    </h3>
                    <p class="text-xs text-slate-500 dark:text-slate-400 mb-4">Export or copy your live generated form code instantly to clipboard or download as HTML.</p>
                    <div class="flex flex-wrap gap-2">
                        <button onclick="copyGeneratedCode()" class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold py-2.5 px-3 rounded-xl transition flex items-center justify-center gap-1.5 shadow-sm">
                            <i id="copyMainIcon" class="fa-solid fa-copy"></i> <span id="copyMainText">Copy HTML Code</span>
                        </button>
                        <button onclick="downloadHtmlFile()" class="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-semibold py-2.5 px-3 rounded-xl transition flex items-center justify-center gap-1.5">
                            <i class="fa-solid fa-download"></i> Download .html
                        </button>
                    </div>
                </div>
            </div>

            <!-- Right Live Preview Panel -->
            <div class="lg:col-span-7">
                <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 overflow-hidden sticky top-24">
                    <div class="bg-slate-100 dark:bg-slate-800 px-6 py-3 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <div class="w-3 h-3 rounded-full bg-rose-500"></div>
                            <div class="w-3 h-3 rounded-full bg-amber-500"></div>
                            <div class="w-3 h-3 rounded-full bg-emerald-500"></div>
                        </div>
                        <span class="text-xs font-mono text-slate-500 dark:text-slate-400">Live Interactive Preview</span>
                    </div>

                    <div class="p-6 sm:p-8" id="previewContainer">
                        <!-- Dynamic preview rendered here -->
                    </div>

                    <!-- Submission Result Box -->
                    <div id="resultBox" class="hidden mx-6 mb-6 p-4 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800 text-sm">
                        <div class="font-bold text-emerald-800 dark:text-emerald-300 mb-1 flex items-center gap-2">
                            <i class="fa-solid fa-circle-check"></i> Form Submitted Successfully!
                        </div>
                        <div id="resultContent" class="text-emerald-700 dark:text-emerald-400 font-mono text-xs space-y-1"></div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Tab 2: Code & Export -->
        <div id="tabCode" class="hidden space-y-6">
            <div class="bg-white dark:bg-slate-900 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 p-6">
                <div class="flex items-center justify-between mb-4">
                    <div>
                        <h2 class="text-lg font-bold flex items-center gap-2 text-emerald-600 dark:text-emerald-400">
                            <i class="fa-solid fa-code"></i> Generated HTML Source Code
                        </h2>
                        <p class="text-xs text-slate-500 dark:text-slate-400">Self-contained, responsive, and ready to paste into any project or web editor.</p>
                    </div>
                    <button onclick="copyCodeViewer()" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold py-2 px-3 rounded-xl transition flex items-center gap-1.5">
                        <i id="codeCopyIcon" class="fa-solid fa-copy"></i> <span id="codeCopyText">Copy Code</span>
                    </button>
                </div>
                <div class="relative">
                    <pre id="codeOutput" class="bg-slate-950 text-slate-200 p-4 rounded-xl text-xs font-mono overflow-x-auto h-[500px] border border-slate-800"></pre>
                </div>
            </div>
        </div>

    </main>

    <footer class="mt-auto py-6 text-center text-xs text-slate-500 border-t border-slate-200 dark:border-slate-800">
        <p>&copy; 2026 TextForm Studio. Built for fast web prototyping & student workflows.</p>
    </footer>

    <script>
        // Theme Toggle
        function toggleTheme() {
            const html = document.documentElement;
            const icon = document.getElementById('themeIcon');
            html.classList.toggle('dark');
            if (html.classList.contains('dark')) {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            } else {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            }
        }

        // Tab Switcher
        function switchTab(tab) {
            const btnBuilder = document.getElementById('btnBuilder');
            const btnCode = document.getElementById('btnCode');
            const tabBuilder = document.getElementById('tabBuilder');
            const tabCode = document.getElementById('tabCode');

            if (tab === 'builder') {
                btnBuilder.className = "px-3 py-1.5 rounded-lg text-sm font-medium bg-emerald-600 text-white shadow-sm transition";
                btnCode.className = "px-3 py-1.5 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition";
                tabBuilder.classList.remove('hidden');
                tabCode.classList.add('hidden');
            } else {
                btnCode.className = "px-3 py-1.5 rounded-lg text-sm font-medium bg-emerald-600 text-white shadow-sm transition";
                btnBuilder.className = "px-3 py-1.5 rounded-lg text-sm font-medium text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition";
                tabCode.classList.remove('hidden');
                tabBuilder.classList.add('hidden');
                generateCodeString();
            }
        }

        // Generate Form HTML String dynamically
        function getFormHtml() {
            const title = document.getElementById('formTitleInput').value || 'Text Form';
            const desc = document.getElementById('formDescInput').value || '';
            const theme = document.getElementById('formTheme').value;
            const align = document.getElementById('buttonAlign').value;

            const hasName = document.getElementById('fieldStudentName').checked;
            const hasRoll = document.getElementById('fieldRollNo').checked;
            const hasSubject = document.getElementById('fieldSubject').checked;
            const hasDate = document.getElementById('fieldDate').checked;
            const hasComments = document.getElementById('fieldComments').checked;

            let accentBg = 'bg-emerald-600 hover:bg-emerald-700';
            if (theme === 'indigo') accentBg = 'bg-indigo-600 hover:bg-indigo-700';
            if (theme === 'amber') accentBg = 'bg-amber-600 hover:bg-amber-700';

            let alignClass = 'text-right';
            if (align === 'left') alignClass = 'text-left';
            if (align === 'full') alignClass = 'text-center';

            let fieldsHtml = '';

            if (hasName) {
                fieldsHtml += `
                <div>
                    <label class="block text-sm font-medium mb-1">Full Name</label>
                    <input type="text" id="inputName" placeholder="Enter full name" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                </div>`;
            }

            if (hasRoll) {
                fieldsHtml += `
                <div>
                    <label class="block text-sm font-medium mb-1">Roll Number / ID</label>
                    <input type="text" id="inputRoll" placeholder="e.g. 2026-TX-041" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                </div>`;
            }

            if (hasSubject) {
                fieldsHtml += `
                <div>
                    <label class="block text-sm font-medium mb-1">Subject / Category</label>
                    <select id="inputSubject" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                        <option value="Fiber Science">Fiber Science Lab</option>
                        <option value="Yarn Testing">Yarn Testing Analysis</option>
                        <option value="Fabric Testing">Fabric Testing Report</option>
                        <option value="General Assignment">General Assignment</option>
                    </select>
                </div>`;
            }

            if (hasDate) {
                fieldsHtml += `
                <div>
                    <label class="block text-sm font-medium mb-1">Submission Date</label>
                    <input type="date" id="inputDate" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none">
                </div>`;
            }

            if (hasComments) {
                fieldsHtml += `
                <div>
                    <label class="block text-sm font-medium mb-1">Notes / Comments</label>
                    <textarea id="inputComments" rows="3" placeholder="Enter observations or remarks..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-transparent text-sm focus:ring-2 focus:ring-emerald-500 outline-none"></textarea>
                </div>`;
            }

            return `
            <div class="space-y-6">
                <div>
                    <h2 class="text-2xl font-bold tracking-tight mb-1">${title}</h2>
                    <p class="text-sm text-slate-500 dark:text-slate-400">${desc}</p>
                </div>
                <form onsubmit="handleFormSubmit(event)" class="space-y-4">
                    ${fieldsHtml}
                    <div class="${alignClass} pt-2">
                        <button type="submit" class="${accentBg} text-white font-semibold text-sm px-6 py-2.5 rounded-xl transition shadow-sm ${align === 'full' ? 'w-full' : ''}">
                            Submit Record
                        </button>
                    </div>
                </form>
            </div>`;
        }

        // Update Live Preview
        function updatePreview() {
            const container = document.getElementById('previewContainer');
            container.innerHTML = getFo
