### Research Plan

To evaluate open-source AI models for assessing student competence in Python, I would begin by surveying freely available LLMs designed for code understanding, such as Code Llama or StarCoder. The evaluation would focus on their ability to analyze student-written Python programs for syntax errors and deeper logical or conceptual issues (e.g., misuse of loops, misunderstanding of recursion, or incorrect handling of edge cases). I would establish criteria for suitability that include: 
(1) the model’s ability to identify both surface-level and conceptual mistakes, 
(2) the clarity and relevance of its feedback, 
(3) its tendency to generate reflective prompts rather than direct solutions, and 
(4) adaptability for integration into educational workflows. 
To test these models, I would feed them a set of common buggy student submissions, then evaluate whether their output produces guiding questions and insights that help students reason through the problem, instead of simply supplying corrections.

A model suitable for high-level competence analysis should demonstrate an ability to link code-level mistakes with underlying misconceptions (e.g., showing that an off-by-one error reflects a misunderstanding of loop boundaries). To validate prompt quality, I would use a rubric assessing whether generated prompts are open-ended, conceptually focused, and supportive of self-discovery. Trade-offs are expected: larger models may deliver more nuanced insights but at the expense of higher compute cost, while smaller ones may be more efficient but less pedagogically sensitive. I highlighted Code Llama as an initial candidate because of its strong performance on code reasoning tasks, permissive license, and active community. Its limitation, however, lies in occasionally defaulting to complete solutions rather than reflective hints, which means additional fine-tuning or careful prompt engineering would be necessary to align it with educational goals.
