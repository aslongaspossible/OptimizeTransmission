# lim0

$x_1=x_2$ is a solution of Eq.~$\eqref{eq_vieta}$ with $\beta=0$, which means that the lattice thermal conductance is zero. For $\beta\rightarrow0$, we suppose that $x_1,x_2{\rightarrow}x_0$ as $\beta\rightarrow0$, and expand Eq.~$\eqref{eq_vieta}$ at $x=x_0$. Appendix \ref{append:lim0} shows more details. We find that, the limit $x_0$ may take its value in three cases: 
1.When $M(x)$ is not continuous at $x_0$, and Eq.~\eqref{eq:cond1} is satisfied;
2. When the derivitive $M'(x)$ is not continuous at $x_0$, and Eq.~\eqref{eq_nobeta3rd} have solution that satisfies $\epsilon_1\epsilon_2\le0$, $\epsilon_2>\epsilon_1$;
3. When $h(x_0)=0$, where auxiliary function $h(x)$ is defined as Eq.~\eqref{eq:defh}.

In case that $M(x)$ is not continuous at $x_0$,  the width for optimal transport window is

\begin{equation}
({\Delta}x)_\text{discontinue}\approx\left(\frac{48\cosh^2(x_0/2)\beta}{\displaystyle\max_{n=-,+}(h_n(x_0)+2M_n(x_0))}\right)^{1/3},
\end{equation}
where $h_{+,-}$ is defined as Eq.~\eqref{eq:defhlim} and $M_{+,-}$ is defined as Eq.~\eqref{eq:defMlim}.

In other two cases that $M(x)$ is continuous at $x_0$, the width for optimal transport window is

\begin{equation}
({\Delta}x)_{C^0}\approx\left(\frac{24\cosh^2(x_0/2)\beta}{M_n(x_0)}\right)^{1/3}.
\end{equation}

There may be more than one limit as $\beta\rightarrow0$. According to Eq.~\eqref{eq_zTx}, the one which gives the smallest ${\Delta}x$ will give the best $zT$. 

Take a special case that $M(x){\equiv}M_0$ is a constant, then the limit $x_0$ satisfies

\begin{equation}
x_0\tanh(x_0/2)=3,
\end{equation}
leads to $x\approx\pm3.24$, which is compatible to Maassen's numerical result\cite{Jesse2021}. Thus,

\begin{align}
(zT)_\text{optimal}\approx 1.39{(M_0/\beta) ^{ \frac{2}{3}}}.
\end{align}
