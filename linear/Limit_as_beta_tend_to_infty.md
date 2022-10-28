# Limit as $\beta\rightarrow\infty$

\textbf{Limit as $\beta\rightarrow\infty$}. According to Maassen's arguement, this is equivalent to maximizing power factor

\begin{equation}
GS^2=\frac{k_\text{B}^2}{h}\frac{I_1^2}{I_0}.
\end{equation}
Do calculus of variations as

\begin{equation}
\begin{split}
{\delta}(GS^2)\approx&\frac{k_\text{B}^2}{h}\left(\frac{2I_1{\delta}I_1}{I_0}-\frac{I_1^2}{I_0^2}{\delta}I_0\right)\\
=&\frac{k_\text{B}^2}{h}\frac{I_1}{I_0^2}{\int}(2xI_0-I_1)M(x){\delta}\mathcal{T}(x)\mathrm{d}x.
\end{split}
\end{equation}
Consider the case $S>0$ ($S<0$ will be similar), when $2xI_0-I_1>0$, a positive ${\delta}\mathcal{T}(x)$ will increase $GS^2$; when $2xI_0-I_1<0$, a negative ${\delta}\mathcal{T}(x)$ will increase $GS^2$. So the best $\mathcal{T}(x)$ for optimized $GS^2$ is a step function

\begin{equation}
\mathcal{T}(x)=\left\{
\begin{aligned}
  1,\ &\text{if }x>I_1/(2I_0);\\
  0,\ &\text{if }x<I_1/(2I_0).
\end{aligned}
\right.
\end{equation}

For a constant $M$, the step opsition can be achieved by solving

\begin{equation}
2x_{\infty}I_0(x_\infty, \infty)=I_1(x_\infty, \infty).
\end{equation}
Numerical solution is $x_\infty=1.145$, which is consistent with Maassen's result\cite{Jesse2021} and Whitney's result of $\exp(-x_\infty)=0.318$\cite{Whitney2014}.
