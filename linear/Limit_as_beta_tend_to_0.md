# Limit as beta tend to 0

$\require{physics}$

\begin{align}
x_1+x_2=2\frac{I_2+\beta}{I_1}\\
x_1x_2=\frac{I_2+\beta}{I_0}
\end{align}

$x_1=x_2$ is a solution to $\beta=0$. When considering $\beta\rightarrow0$, we suppose the solution may be $x_2=x_1+{\Delta}x$. $\beta$ and ${\Delta}x$ may not be same order infinitesimals, so first we get rid of $\beta$:

$$
\frac{x_1+x_2}{2}I_1=x_1x_2I_0,
$$

thus

\begin{equation}
\left(x_1+\frac{{\Delta}x}{2}\right)I_1=x_1(x_1+{\Delta}x)I_0.
\end{equation}

Compare coefficient of same order infinitesimals, we get a serial of equations. First two are trivailly $0=0$, while third order infinitesimals give us:

\begin{equation}
x_1\left(\tanh\left(\frac{x_1}{2}\right)-\frac{M'(x_1)}{M(x_1)}\right)=3.
\end{equation}

In the case of $M$ equals a constant, $M'=0$, so we can solve the equation $x_1\tanh(x_1/2)=3$ and get the limit $x_1\approx3.24$, which is compatible to Maassen's numerical result\cite{Jesse2021}.