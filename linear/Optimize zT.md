# 优化 $zT$ 的方法

[TOC]

## 把 $zT$ 写作能带的泛函

根据 [Mahan](https://doi.org/10.1073/pnas.93.15.7436) 的工作，
$$
zT = \frac{I_{1}^{2}}{I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha }
$$
其中
$$
I_{n}=\int_{-\infty}^{+\infty} \mathrm{d} x \frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} s(x) x^{n}
$$

$$
s(x)=\hbar a_{0} \Sigma\left(\mu+x k_{B} T\right)
$$

## Landauer 公式

根据 [Changwook Jeong](https://doi.org/10.1063/1.3291120) 的工作，
$$
\Sigma(\varepsilon)=\mathcal{T}(\varepsilon)M(\varepsilon)
$$
其中 $M(\varepsilon)$ 正比于通道数，$0\le \mathcal{T}(\varepsilon)\le 1$ 是透射谱。$\mathcal{T}(\varepsilon)$ 可以理解为自由程与样品长度的比。因此自由程越短电阻越大。这与 有效质量越大→自由程越短&迁移率越低→电阻越大 是相符合的。

## 变分

考虑最简单的情况，假定通道数是常数 $M(\varepsilon)=\text{Constant}$，即
$$
s(x)=A\mathcal{T}(x)
$$
通道数不能看作常数的情况在[后面](Optimize%20zT.md#%E5%AF%B9%E9%80%9A%E9%81%93%E6%95%B0%E4%B8%8D%E4%B8%BA%E5%B8%B8%E6%95%B0%E7%9A%84%E8%AE%A8%E8%AE%BA)讨论。对 $zT$ 变分，也就是令 $\mathcal{T}(x)\rightarrow \mathcal{T}(x)+\delta \mathcal{T}(x)$ 后考察泛函的变化，保留到 $\delta \mathcal{T}(x)$ 的一阶项。则
$$
\delta I_{n}=\int_{-\infty}^{+\infty} \mathrm{d} x \frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} A x^{n}\delta \mathcal{T}(x)
$$
由于 $zT$ 不含$\mathcal{T}(x)$ 的导数，所以变分和求导完全一样：
$$
\begin{split}
\delta zT &= \frac{2I_{1}\delta I_1}{I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha }-\frac{I_{1}^{2}}{\left(I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha\right)^2}\left(I_2\delta I_0+I_0\delta I_2-2I_1\delta I_1+\delta I_0/\alpha\right)\\
&=\frac{2I_1I_0\left(I_2+1/\alpha\right)\delta I_1-I_1^2\left(\left(I_2+1/\alpha\right)\delta I_0+I_0\delta I_2\right)}{\left(I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha\right)^2}\\
&=\frac{I_1^2I_0}{\left(I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha\right)^2}\left(2\frac{I_2+1/\alpha}{I_1}\delta I_1-\left(\delta I_2+\frac{I_2+1/\alpha}{I_0}\delta I_0\right)\right)\\
&=\frac{I_1^2I_0}{\left(I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha\right)^2}\int_{-\infty}^{+\infty} \mathrm{d} x \frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} A\left(2\frac{I_2+1/\alpha}{I_1}x-\left(x^2+\frac{I_2+1/\alpha}{I_0}\right)\right)\delta \mathcal{T}(x)
\end{split}
$$
于是发现，仅当 $x$ 满足
$$
f(x)\equiv2\frac{I_2+1/\alpha}{I_1}x-\left(x^2+\frac{I_2+1/\alpha}{I_0}\right)=0
$$
时，$\delta \mathcal{T}(x)$ 可以任意取值而不影响 $zT$。而当 $f(x)>0$ 时，取 $\delta \mathcal{T}(x)>0$ 可以增加 $zT$；当 $f(x)<0$ 时，取 $\delta \mathcal{T}(x)<0$ 可以增加 $zT$。这也就是说，最优的透射谱是方形的：当 $f(x)>0$ 时，$\mathcal{T}(x)=1$；当 $f(x)<0$ 时，$\mathcal{T}(x)=0$。

## 透射谱及最优的 $zT$

假设透射谱在能量窗口 $(x_1, x_2)$ 内是 $1$，之外是 $0$。则 $I_n$ 变为 $x_1, x_2$ 的函数。又，$x_1, x_2$ 满足 $f(x)=0$，这样就得到了关于 $x_1, x_2$ 的方程组：
$$
\begin{align}
x_1+x_2&=2\frac{I_2+1/\alpha}{I_1}\\
x_1x_2&=\frac{I_2+1/\alpha}{I_0}
\end{align}
$$
可以数值求解这两个方程组。$\alpha, A$ 是方程组的两个参数。事实上只需要一个参数就够了，只要令
$$
I_n'=I_n/A
$$
这样的 $I_n'$ 就与 $A$ 无关，而方程组变为
$$
\begin{align}
x_1+x_2&=2\frac{I_2'+1/\alpha A}{I_1'}\label{xplus}\\
x_1x_2&=\frac{I_2'+1/\alpha A}{I_0'}\label{xmulti}
\end{align}
$$

$zT$ 的表达式变为
$$
\begin{split}
zT &= \frac{I_{1}'^{2}}{I_{2}'I_{0}'-I_{1}'^{2}+I_{0}'/\alpha A}=\frac{I_{1}'/I_0'}{\frac{I_2'+1/\alpha A}{I_1'}-I_{1}'/I_{0}'}\\
&=\frac{2x_1x_2/(x_1+x_2)}{(x_1+x_2)/2-2x_1x_2/(x_1+x_2)}=\frac{4x_1x_2}{\left(x_2-x_1\right)^2}
\end{split}
$$
通过数值计算，可以对一系列的 $\alpha A$ 的取值来计算可能的最优的 $zT$。计算结果见附图。对于我们想要找的 $zT\ge 3$ 的材料来说，最优的透射谱是让透射窗口在费米面上（或下）$1.9\sim 5.9\ k_\text{B}T$ 之间，取 $300\text{ K}$ 也就是 $0.05\sim 0.15\ e\text{V}$。这已经很接近 $\delta$ 函数了。

# Landauer 公式的微观解释

## 确定系数

在 [Mahan](https://doi.org/10.1073/pnas.93.15.7436) 的工作中，
$$
\Sigma(\varepsilon)=\sum_{\mathbf{k}}v_x(\mathbf{k})^2\tau(\mathbf{k})\delta(\varepsilon-\varepsilon(\mathbf{k}))
$$
实际上是错的。这不影响上面的讨论，但是如果要定出系数 $A$，就需要重新考察这个式子了。[Changwook Jeong](https://doi.org/10.1063/1.3291120) 的工作是接着 [Mahan](https://doi.org/10.1073/pnas.93.15.7436) 的工作做的，而他的文章反而给出的是正确的公式。

在固体物理中，固体的体积越大，允许的 Bloch 波矢 $\mathbf{k}$ 越密。因此，对同样一种材料，如果取的样品体积越大，${\displaystyle \sum_{\mathbf{k}}}$ 越大；那么，如果按照这个理论来看 Mahan 的这个工作，就会发现电导率、电子热导率随着体积的增加而增大，这显然是不对的。实际上，取
$$
\Sigma(\varepsilon)=\frac{1}{V}\sum_{\mathbf{k}}v_x(\mathbf{k})^2\tau(\mathbf{k})\delta(\varepsilon-\varepsilon(\mathbf{k}))
$$
就可以了（不证）。而一般来说，考虑体积无限大的极限， $\frac{1}{V}\sum_{\mathbf{k}}$ 可以用 $\frac{1}{4\pi^3}\int \mathrm{d}\mathbf{k}$ 来代替（如果自旋简并），这里也是一样（不证）。Mahan 和 Jeong 的公式的区别有两个：Mahan 漏掉了 $1/V$；Jeong 算的是电导、热导，而非电导率、热导率。因此，对 Mahan 给出的公式，只要乘以因子 $V^{-1}\cdot S/L=L^{-2}$，就可以和 Jeong 的公式对上。

接下来确定 $A$ 的过程与 [Changwook Jeong](https://doi.org/10.1063/1.3291120) 的工作几乎完全一样：
$$
\begin{split}
V^{-1}\Sigma(\varepsilon)&=\frac{1}{4\pi^3}\int \mathrm{d}\mathbf{k}v_x(\mathbf{k})^2\tau(\mathbf{k})\delta(\varepsilon-\varepsilon(\mathbf{k}))\\
&=\frac{\int \mathrm{d}\mathbf{k}v_x(\mathbf{k})^2\tau(\mathbf{k})\delta(\varepsilon-\varepsilon(\mathbf{k}))}{\int \mathrm{d}\mathbf{k}|v_x(\mathbf{k})|\delta(\varepsilon-\varepsilon(\mathbf{k}))}\cdot\frac{1}{4\pi^3}\int \mathrm{d}\mathbf{k}|v_x(\mathbf{k})|\delta(\varepsilon-\varepsilon(\mathbf{k}))\\
&=\frac{\left<v_x^2\tau\right>}{\left<|v_x|\right>}\cdot\frac{1}{4\pi^3}\int \mathrm{d}\mathbf{k}|v_x(\mathbf{k})|\partial_\varepsilon\int^\varepsilon\mathrm{d}\varepsilon'\delta(\varepsilon'-\varepsilon(\mathbf{k}))\\
&=\frac{\left<v_x^2\tau\right>}{\left<|v_x|\right>}\cdot\frac{1}{4\pi^3}\int\mathrm{d}\mathbf{k}|v_x(\mathbf{k})|\partial_\varepsilon\theta(\varepsilon-\varepsilon(\mathbf{k}))\\
&=\frac{\left<v_x^2\tau\right>}{\left<|v_x|\right>}\cdot\frac{1}{4\pi^3}\int\mathrm{d}k_y\mathrm{d}k_z\partial_\varepsilon\int\mathrm{d}k_x\left|\frac{\partial\varepsilon(\mathbf{k})}{\partial\hbar k_x}\right|\theta(\varepsilon-\varepsilon(\mathbf{k}))\\
&=\frac{\left<v_x^2\tau\right>}{\left<|v_x|\right>}\cdot\frac{1}{4\pi^3\hbar}\int\mathrm{d}k_y\mathrm{d}k_z\Xi_x(\varepsilon,k_y,k_z)\\
&=\frac{\left<v_x^2\tau\right>}{\left<|v_x|\right>}\cdot\frac{1}{\pi\hbar}\cdot \frac{1}{a_ya_z}\cdot \left<\Xi_x\right>_\varepsilon
\end{split}
$$

[Changwook Jeong](https://doi.org/10.1063/1.3291120) 说，其中 $\left<v_x^2\tau\right>/\left<|v_x|\right>$ 这一项可以认为是自由程，而自由程不可能超过材料的纵向长度 $L$。如果定义 $\mathcal{T}=(\left<v_x^2\tau\right>/\left<|v_x|\right>)/L$ ，则 $0\le T\le 1$。因此
$$
s(x)=\hbar a_0\Sigma=\mathcal{T}(x)L\frac{a_0\left<\Xi_x\right>}{\pi a_ya_z}
$$
即 $A=La_0\left<\Xi_x\right>/\pi a_ya_z$。

上面只是对单条能带的讨论。对多条能带，等同于并联，$A$ 应该理解为所有带的贡献的叠加。这其实等价于把 $\Xi_x(\varepsilon)$ 理解成所有能带与 $E=\varepsilon$ 的交点的总和。

从 $A$ 的表达式来看，似乎扩胞会降低 $A$；但扩胞会增加能带的数量，也就是会增加最终总的 $A$；比如，在 $y$ 方向扩一倍，$a_y$ 变成两倍，要叠加的能带个数变成两倍，最后其实没有影响。

## 对通道数不为常数的讨论

上面的讨论默认通道数 $\left<\Xi_x\right>$ 与能量无关。对于我们想要找的 $zT\ge 3$ 的材料来说，$300\text{ K}$ 下，透射窗口为 $4\ k_\text{B}T\approx 0.1e\text{V}$ ，在这个范围内要求通道数随着能量基本不变还是比较合理的。

此外，即便通道数变化比较剧烈，上面的讨论（在某种意义上）也是有用的。理论修改为
$$
s(x)=A'\Xi_x(x)\mathcal{T}(x)
$$
其中 $\Xi_x(x)$ 就是[前面](Optimize%20zT.md#%E7%A1%AE%E5%AE%9A%E7%B3%BB%E6%95%B0)的 $\left<\Xi_x\right>_\varepsilon$。对 $\mathcal{T}(x)$ 变分：
$$
\delta zT=\frac{I_1^2I_0}{\left(I_{2}I_{0}-I_{1}^{2}+I_{0}/\alpha\right)^2}\int_{-\infty}^{+\infty} \mathrm{d} x \frac{\mathrm{e}^{x}}{\left(\mathrm{e}^{x}+1\right)^{2}} A'\Xi_x(x)\left(2\frac{I_2+1/\alpha}{I_1}x-\left(x^2+\frac{I_2+1/\alpha}{I_0}\right)\right)\delta \mathcal{T}(x)
$$
与[之前的变分](Optimize%20zT.md#%E5%8F%98%E5%88%86)形式几乎一样，只不过这次 $I_n$ 的积分中体现了$\Xi_x(x)$ 的变化。因此，如果给定透射谱，仍然能够列出像[上面那样的方程组](#透射谱及最优的 $zT$)。

# 讨论

## 透射谱真的完全可调吗？

上面这套理论当中，核心是变分；所对应的物理过程是，对于给定晶格热导率的材料，通过声子散射或者别的方法，让透射谱变成只在某个能量窗口能透过的形状。但是实际上，想提升透射率到 $1$ 好像没有实现方法。此外，让能量窗口之外的透射率完全降到 $0$ 好像也不是能够实现的事情。

另外，态密度变大会导致平均自由程变小。

反过来说，也可以先找到符合的透射谱。但是实际上透射谱的形状不是充分条件，窗口的位置更关键。即便不是完美的方形，只要通过 $f(x)=0$ 计算出窗口的位置，窗口之内透射率高，窗口之外透射率低，就能够有比较高的 $zT$。

因此，这套理论的用处在于给出一个快速筛查的方法，比如看透射率和窗口的匹配程度；找 $\alpha A$ 更大的材料，等等。

## 无量纲参数 $\alpha A$ 怎么指导材料设计？

根据计算结果， $\alpha A$ 越大越好。但是其实 $\alpha A$ 很难算：

### 晶格热导率难算

$\alpha$ 中唯一由材料决定的是 $\kappa_\ell $，计算量超大。通常的方法有冻声子法、DMFT，都算得不太快，不适合做材料筛查。[Lihua Chen](https://doi.org/10.1016/j.commatsci.2019.109155) 用机器学习学了一个模型，但他们的训练集 100 测试集 5，可能不是很靠谱。

### $L$ 难以确定

如前所述，$L$ 是材料的尺寸。它的作用是给自由程一个上限，这样才能够对 $zT$ 求最大值。但是这个上限要怎么给，是完全不知道的。引入 $L$ 的是 [Changwook Jeong](https://doi.org/10.1063/1.3291120)，他们莫名其妙地把 $L$ 给消掉了。我们完全可以预估一个自由程的上限，或者认为 $L$ 是 Landauer 公式还能适用的尺度，这样上面的讨论还都能成立；但那样的话，就没有办法根据 $\alpha A$ 来做材料设计，因为现在这个参数是完全经验性的了。

## $A$ 和 $zT$ 在纳米尺度的重新理解

如果把前文所有 电导率/热导率 都理解成 电导/热导，然后把 $A$ 就简单地理解成能够通过电子个数的上限，而且把它理解成一个实验测量量，那么倒是可以绕开这个问题。但是这样的话就要重新考察 $zT$ 是否还能够表征热电转化效率了。

在纳米尺度，只有电导/热导有意义而不是电导率/热导率的情况下，$zT$ 还能表征热电转化效率吗？如果不能的话，新的表达形式是什么？

实际上，如果 $\mathcal{T}$ 可调的话，那么 $KR$ 就不再是一个定值了。所以其实调 $\mathcal{T}$ 应该看作等价于换材料。

如果认为调整体材料的尺寸可以看作是在调 $A$，那么 $zT$ 这一套理论还是能用的。

## 是否会得到超出量子力学确定的上限？

[Whitney](https://doi.org/10.1103/PhysRevB.91.115425) 给出了量子体系的功率&效率上限，以及最大功率下的效率(45)。

但是 最大功率下的效率(45) 是在没有电阻信息的情况下给出的，这个 最大功率 的条件与通常线性响应的 $zT$ 给出来的一定是不同的，所以最后效率也不是在同样条件下的效率。

## 当 $\alpha'M_0\rightarrow+\infty$ 时的 $x_1,x_2$ 的极限

 假设 $x_1=x,x_2=x+\varepsilon$，接下来就是要在 $\varepsilon\rightarrow0$ 处展开。由于 $\alpha'M_0$ 的阶次比 $\varepsilon$ 高，高几阶不确定；因此我们先把 $\alpha'M_0$ 消掉再展开：
$$
\begin{equation}
 \frac{x_1+x_2}{2}\overline{I_0'}=x_1x_2\overline{I_1'}\label{serialtot}
 \end{equation}
$$

 其中把 $\overline{I_n'}$ 替换为展开到三阶的泰勒级数：
$$
 \overline{I_n'}\approx\sum_{k=1}^{3}\frac{f_n^{(k-1)}}{k!}\varepsilon^k
$$

一些有用的公式：
$$
\begin{align*}
s\equiv&\tanh\left(\frac{x}{2}\right)\\
s'=&2f_0\\
f_n'=&nf_{n-1}-sf_n\\
f_n''=&n(n-1)f_{n-2}-2nsf_{n-1}+(s^2-2f_0)f_n\\
f_n^{(3)}=&n(n-1)(n-2)f_{n-3}-3n(n-1)sf_{n-2}+3n(s^2-2f_0)f_{n-1}+(8sf_0-s^3)f_n
\end{align*}
$$

 一阶和二阶都是 trivial 的；三阶的结果是
$$
 x\tanh\left(\frac{x}{2}\right)=3
$$
于是我们得到极限为 $x=3.24363735$。同样地，把 $\eqref{xmulti}$ 展开到三阶，可以得到
$$
\frac{1}{\alpha'M_0}=\frac{f_0}{3!}\varepsilon^3=0.00606429\cdot\varepsilon^3
$$

实际上，更高阶的 $\eqref{serialtot}$ 的展开的形式为：
$$
xf_0^{(k-2)}=-kf_0^{(k-3)}
$$
四阶以上就不满足了。

# 总结

上面的方法给出的有用的结论只有：

- Mahan 的结论大体上没错，要找透射谱尽可能窄的材料，透射窗口的宽度大概在 $0.1\ e\text{V}$。峰的中心位置并不是像 Mahan 说的那样离费米面 $2.4\ k_\text{B}T$，而是大约 $3.9\ k_\text{B}T\approx 0.1\ e\text{V}$。
- 声子对电子的散射并不是越强越好。实际上，应该在透射窗口之外越强越好，窗口之内反而要弱。
- 晶格热导率越低越好，在输运方向垂直的面上晶格常数越小（原胞越多）越好，通道数越多越好。

# References

1. [PNAS July 23, 1996 93 (15) 7436-7439](https://doi.org/10.1073/pnas.93.15.7436)
2. [J. Appl. Phys. **107**, 023707 (2010)](https://doi.org/10.1063/1.3291120)
3. [DOI: 10.1016/j.commatsci.2019.109155](https://doi.org/10.1016/j.commatsci.2019.109155)

