# Limit as beta tend to 0

$\require{physics}$

\begin{align}
x_1+x_2=2\frac{I_2+\beta}{I_1}\\
x_1x_2=\frac{I_2+\beta}{I_0}\label{eq_vieta}
\end{align}

$x_1=x_2$ is a solution of Eq.~$\eqref{eq_vieta}$ with $\beta=0$, which means the lattice thermal conductance is zero. For $\beta\rightarrow0$, we suppose the solution may has the form

\begin{equation}
x_1=x_0+\epsilon_1,x_2=x_0+\epsilon_2 ,\label{eq_asymx}
\end{equation}

where $\epsilon_1,\epsilon_2$ are infinitesimals, and ${\Delta}x=\epsilon_2-\epsilon_1>0$. $\beta$ and ${\Delta}x$ may not be same-order infinitesimals, so first we get rid of $\beta$ from Eq.~$\eqref{eq_vieta}$:


\begin{equation}
\frac{x_1+x_2}{2}I_1=x_1x_2I_0,
\end{equation}


thus

\begin{equation}
\begin{split}
&\left(x_0+\frac{\epsilon_2-\epsilon_1}{2}\right)I_1(x_0+\epsilon_1,x_0+\epsilon_2)\\
&=(x_0+\epsilon_1)(x_0+\epsilon_2)I_0(x_0+\epsilon_1,x_0+\epsilon_2).
\end{split}\label{eq_nobeta}
\end{equation}

Suppose $M(x)$ is analytical in some vicinity $(x_0-\delta,x_0)\cup(x_0, x_0+\delta)$, we can expand above equation to Tylor series at $x_0$. By comparing coefficients of same-order infinitesimals, we get a serial of equations. First order is trivial identity, while the second-order infinitesimals lead to:

\begin{equation}
(M_1(x_0)-M_2(x_0))\epsilon_1\epsilon_2=0,\label{eq_nobeta2nd}
\end{equation}
where 

\begin{equation}
M_n(x)=\lim_{\epsilon_n\rightarrow0}M(x+\epsilon_n)=\left\{\begin{aligned}
M(y)|_{y{\rightarrow}x^-}\text{ if }\epsilon_n<0,\\
M(y)|_{y{\rightarrow}x^+}\text{ if }\epsilon_n>0.
\end{aligned}\right.
\end{equation}

If $M_1(x_0)=M_2(x_0)$, which means that $\epsilon_1\epsilon_2\ge0$ or $M(x)$ is continuous at $x_0$, Eq.~\eqref{eq_nobeta2nd} is also trivial identity and we may have to study third order terms: 

\begin{equation}
\epsilon_1^2(\epsilon_2-\epsilon_1/3)h_1(x_0)-\epsilon_2^2(\epsilon_1-\epsilon_2/3)h_2(x_0)=0,\label{eq_nobeta3rd}
\end{equation}
where

\begin{equation}
h(x){\equiv}x\left({M(x)\tanh\left({x}/{2}\right)-{M'(x)}}\right)-3M(x), 
\end{equation}
$M'(x)$ is the derivative of $M(x)$, and

\begin{equation}
h_n(x)=\left\{\begin{aligned}
h(x)|_{x{\rightarrow}x^-}\text{ if }\epsilon_n<0,\\
h(x)|_{x{\rightarrow}x^+}\text{ if }\epsilon_n>0.
\end{aligned}\right.
\end{equation}

By expanding Eq.~$\eqref{eq_vieta}$ to Tylor series, we find that first order is zero; second order leads to

$$
\beta_2=\frac{M_2(x_0)-M_1(x_0)}{8\cosh^2(x_0/2)}x_0\epsilon_1\epsilon_2=0,
$$
the last equality is from Eq.~$\eqref{eq_nobeta2nd}$. So leading term is third order infitestimal:

\begin{equation}
\beta\approx\beta_3=\frac{(h_2(x_0)+2M_2(x_0))\epsilon_2^2(\epsilon_2-3\epsilon_1)-(h_1(x_0)+2M_1(x_0))\epsilon_1^2(\epsilon_1-3\epsilon_2)}{48\cosh^2(x_0/2)}.\label{eq_beta3}
\end{equation}

## In case that $M_1(x_0){\neq}M_2(x_0)$

If $M(x)$ is not continuous at $x_0$, which is a common case in 1-dimensional band, Eq.~$\eqref{eq_nobeta2nd}$ gives non trivial equality

\begin{align}
\epsilon_1\epsilon_2=0,
\end{align}
which means that one of $\epsilon_1,\epsilon_2$ is zero. If $\epsilon_1=0$, then ${\Delta}x=\epsilon_2$, $M_2(x_0)=M_+(x_0){\equiv}M(x)|_{x{\rightarrow}x_0^+}$ and $h_2(x_0)=h_+(x_0)$; if $\epsilon_2=0$, then ${\Delta}x=-\epsilon_1$, $M_1(x_0)=M_-(x_0)$ and $h_1(x_0)=h_-(x_0)$.

Eq.~$\eqref{eq_beta3}$ leads to

\begin{equation}
\beta\approx
\frac{(h_n(x_0)+2M_n(x_0))}{48\cosh^2(x_0/2)}({\Delta}x)^3,
\end{equation}
$n=+$ if $\epsilon_1=0$, $n=-$ if $\epsilon_2=0$. Notice that $\beta>0$, so if both $h_n(x_0)+M_n(x_0)<0$ ($n=+,-$), then $x_0$ is not a limit as $\beta\rightarrow0$; if both $h_n(x_0)+M_n(x_0)>0$, then either $\epsilon_1\neq0$ or $\epsilon_2\neq0$ gives local maximum, while global maximum is the one which gives higher $zT$:

\begin{equation}
(zT)_\text{optimal}\approx \frac{4x_0 ^2}{({\Delta}x)^2}
\approx 4x_0 ^2\left(\frac{{\displaystyle\max_{n=+,-}}(h_n(x_0)+2M_n(x_0))}{48\cosh^2(x_0/2)\beta}\right)^{\frac{2}{3}}.
\end{equation}

In conclusion, when $M(x)$ is not continuous at $x_0$, $x_0$ may be a limit if $\max_{n=+,-}(h_n(x_0)+2M_n(x_0))>0$; optimal $zT$ will be

\begin{equation}
(zT)_\text{optimal}=4x_0^2/({\Delta}x)_\text{optimal}^2,
\end{equation}
where

\begin{equation}
({\Delta}x)_\text{optimal}\approx\left(\frac{48\cosh^2(x_0/2)\beta}{\displaystyle\max_{n=-,+}(h_n(x_0)+2M_n(x_0))}\right)^{1/3}
\end{equation}
is the width of optimal transport window.

## In case that $M_1(x_0)=M_2(x_0)$

In case that $\epsilon_1\epsilon_2>0$, or $\epsilon_1\epsilon_2<0$ but $M(x)$ is continuous at $x_0$, the second order expansion $\eqref{eq_nobeta2nd}$ gives trivial identity. Equality from third order terms $\eqref{eq_nobeta3rd}$ should be followed. Substitute Eq.~$\eqref{eq_nobeta3rd}$ into Eq.~$\eqref{eq_beta3}$, we get

\begin{equation}
\beta\approx\frac{M(x_0)}{24\cosh^2(x_0/2)}({\Delta}x)^3.
\end{equation}

Then, according to Eq.~$\eqref{eq_zTx}$, the optimal $zT$ is

\begin{equation}
(zT)_\text{optimal} \approx 4x_0 ^2{\left( {\frac{{24{{\cosh }^2}({x_0 }/2)}}{M(x_0)}\beta } \right)^{ - \frac{2}{3}}}.
\end{equation}

### In case that $M'_1(x_0)=M'_2(x_0)$

If $\epsilon_1\epsilon_2>0$, or $\epsilon_1\epsilon_2<0$ but $M(x)$ and $M'(x)$ are continuous at $x_0$, then Eq.~$\eqref{eq_beta3}$ becomes

$$
h(x_0)(\epsilon_2-\epsilon_1)^3=0.
$$
By assumption, $\epsilon_2-\epsilon_1>0$, so third order term just gives us 

\begin{equation}
h(x_0)=0.
\end{equation} 

In the case that $M$ equals a constant, $M'=0$, so $h(x_0)=0$ gives us $x_0\tanh(x_0/2)=3$ and the limit 

$$
x_0\approx3.24,
$$
which is compatible to Maassen's numerical result\cite{Jesse2021}. Thus,

\begin{align}
(zT)_\text{optimal}\approx 1.39{(M(x_0)/\beta) ^{ \frac{2}{3}}}.
\end{align}
For a spin-degenerate one-band system, $M\equiv2$, and thus

\begin{align}
(zT)_\text{optimal}\approx 2.21\beta^{ -\frac{2}{3}}.
\end{align}
