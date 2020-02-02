#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

#todo 에듀넷 연구대회 타이틀 가져오기 /
html = '''






















<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16665|A009900003|187905|B101000004|20171122|70601|1|6" class="goDetail">
						<td class="num">6</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명교육 활성화를 통한 발명인재 싹 틔우기

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">213</td>
					</tr>

					<tr id="16665|A009900003|187904|B101000004|20171122|70600|2|5" class="goDetail">
						<td class="num">5</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									거꾸로 수업 활용 G.R.I.M. 발명교육 프로그램을 통한 G-Learning 활성화 방안 연구

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">82</td>
					</tr>

					<tr id="16665|A009900003|187903|B101000004|20171122|70599|3|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명교육시범학교 운영을 통한 발명교육 실천사례

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">39</td>
					</tr>

					<tr id="16665|A009900003|187902|B101000004|20171122|70598|4|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									안전교육과 융합한 발명교육 프로그램 개발 및 적용을 통한 초등학교 1, 2학년의 발명태도 함양

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">57</td>
					</tr>

					<tr id="16665|A009900003|187901|B101000004|20171122|70597|5|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명기반 STEAM 프로그램이 초등학생의 융합인재소양에 미치는 효과

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">60</td>
					</tr>

					<tr id="16665|A009900003|187900|B101000004|20171122|70596|6|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									자유학기제 발명, 과학, 진로의 연계 프로그램

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2017년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2017-11-22</td>
						<td class="num">30</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>

























<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16507|A009900003|182724|A000000020|20161020|58065|1|5" class="goDetail">
						<td class="num">5</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2016년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2016년 전국교원 발명교육 연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-10-20</td>
						<td class="num">287</td>
					</tr>

					<tr id="16507|A009900003|182723|A000000020|20161020|58064|2|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2016년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2016년 전국교원 발명교육 연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-10-20</td>
						<td class="num">77</td>
					</tr>

					<tr id="16507|A009900003|182722|A000000020|20161020|58063|3|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2016년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2016년 전국교원 발명교육 연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-10-20</td>
						<td class="num">48</td>
					</tr>

					<tr id="16507|A009900003|182721|A000000020|20161020|58062|4|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2016년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2016년 전국교원 발명교육 연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>고등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-10-20</td>
						<td class="num">49</td>
					</tr>

					<tr id="16507|A009900003|182720|A000000020|20161020|58061|5|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2016년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2016년 전국교원 발명교육 연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-10-20</td>
						<td class="num">125</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>

























<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16235|A009900003|180960|A000000020|20160127|54490|1|8" class="goDetail">
						<td class="num">8</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">500</td>
					</tr>

					<tr id="16235|A009900003|180959|A000000020|20160127|54489|2|7" class="goDetail">
						<td class="num">7</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">244</td>
					</tr>

					<tr id="16235|A009900003|180958|A000000020|20160127|54488|3|6" class="goDetail">
						<td class="num">6</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">131</td>
					</tr>

					<tr id="16235|A009900003|180957|A000000020|20160127|54487|4|5" class="goDetail">
						<td class="num">5</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">93</td>
					</tr>

					<tr id="16235|A009900003|180956|A000000020|20160127|54486|5|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">96</td>
					</tr>

					<tr id="16235|A009900003|180955|A000000020|20160127|54485|6|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">90</td>
					</tr>

					<tr id="16235|A009900003|180954|A000000020|20160127|54484|7|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">89</td>
					</tr>

					<tr id="16235|A009900003|180953|A000000020|20160127|54483|8|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									2015년도 전국교원발명교육연구대회 입상작 보고서

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2015년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2016-01-27</td>
						<td class="num">108</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>

























<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16234|A009900003|178602|A000000020|20150716|46277|1|6" class="goDetail">
						<td class="num">6</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									역량기반 발명융합교육프로그램 개발을 통한 학생창의력대회 지도방안

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-16</td>
						<td class="num">121</td>
					</tr>

					<tr id="16234|A009900003|178545|A000000020|20150710|46194|2|5" class="goDetail">
						<td class="num">5</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									창의적 체험활동 활성화를 위한 발명중심 IMS 융합프로그램 개발 및 적용

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-10</td>
						<td class="num">138</td>
					</tr>

					<tr id="16234|A009900003|178544|A000000020|20150710|46193|3|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									협력적 문제 해결력 신장 프로그램을 통한 발명영재교육원 활성화 방안에 대한 연구

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-10</td>
						<td class="num">57</td>
					</tr>

					<tr id="16234|A009900003|178542|A000000020|20150707|46189|4|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명아이디어플랫폼(2IP)운영을 통한 학교발명반 활성화방안

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">64</td>
					</tr>

					<tr id="16234|A009900003|178515|A000000020|20150707|46162|5|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									초등학교 저학년의 발명동기 향상을 위한 스토리텔링 발명교육프로그램 개발 및 적용

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">86</td>
					</tr>

					<tr id="16234|A009900003|178514|A000000020|20150707|46161|6|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									대한민국학생창의력챔피언대회 본선 학생들의 MBTI 검사를 통한 특성 비교 분석

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2014년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">37</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>

























<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16233|A009900003|178513|A000000020|20150707|46160|1|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									전환기 학생을 위한 징검다리 발명교육 프로그램 개발 및 적용

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2013년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">49</td>
					</tr>

					<tr id="16233|A009900003|178512|A000000020|20150707|46159|2|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명과 과학의 융합활동을 통한 초등학교 발명동아리 활성화 방안에 대한 연구

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2013년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">92</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>

























<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>



					<tr id="16232|A009900003|178511|A000000020|20150707|46158|1|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명동아리 운영 및 지도사례 &#39;스팀에 발명을 얹어 창의력 기르기&#39;

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2012년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">57</td>
					</tr>

					<tr id="16232|A009900003|178510|A000000020|20150707|46157|2|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									창의력대회 현황분석과 대한민국학생창의력챔피언대회를 통한 창의력 신장

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2012년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>중학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">19</td>
					</tr>

					<tr id="16232|A009900003|178509|A000000020|20150707|46156|3|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									렌즐리의 3부 심화학습모형을 적용한 발명동아리운영

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2012년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>고등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">34</td>
					</tr>

					<tr id="16232|A009900003|178494|A000000020|20150707|46141|4|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									&lt;Ⅰ·Greeny&gt; 활동을 통한 발명 교육 활성화 방안

								</a>
							</span>
						</td>
						<td><span class="th_title">대회명</span>2012년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>초등학교</td>
						<td class="line2"><span class="th_title">교과</span>기타</td>
						<td class="line2"><span class="th_title">등록일</span>2015-07-07</td>
						<td class="num">66</td>
					</tr>




	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>

		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>

</div>



		<div class="pagingNav up noPageNav" id="pagingBar">



					<strong>1</strong>




		</div>







      

















<table class="board_list" summary="연구대회별 입상작 번호, 지역, 자료명, 대회명, 등급, 학교급, 교과, 등록일, 조회수의 정보를 제공">
	<caption class="hidden">연구대회별 입상작 목록</caption>
	<colgroup>
		<col width="8%"/>
		<col width="5%"/>
		<col width="*%"/>
		<col width="20%"/>
		<col width="5%"/>
		<col width="8%"/>
		<col width="10%"/>
		<col width="12%"/>
		<col width="7%"/>
	</colgroup>
	<thead>
		<tr>
			<th>번호</th>
			<th>지역</th>
			<th>자료명</th>
			<th>대회명</th>
			<th>등급</th>
			<th>학교급</th>
			<th>교과</th>
			<th>등록일</th>
			<th>조회수</th>
		</tr>
	</thead>
	<tbody>
		
			
				
					<tr id="13012|A009900003|38177|B100600883|20120510|26551|1|8" class="goDetail">
						<td class="num">8</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									SCAMPER 기법을 활용한 쉽고 창의적인 발명 프로젝트 수업 제안
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">215</td>
					</tr>
				
					<tr id="13012|A009900003|38176|B100600883|20120510|26550|2|7" class="goDetail">
						<td class="num">7</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									시뮬레이션을 이용한 창의발명교육 프로그램 가이드북
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">213</td>
					</tr>
				
					<tr id="13012|A009900003|38175|B100600883|20120510|26549|3|6" class="goDetail">
						<td class="num">6</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									타 영역과 융합한 발명교육 지도방안
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">167</td>
					</tr>
				
					<tr id="13012|A009900003|38174|B100600883|20120510|26548|4|5" class="goDetail">
						<td class="num">5</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									발명특허기초 프로그램의 현장 적용·운영을 통한 창의적 체험 활동 활성화 방안
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">80</td>
					</tr>
				
					<tr id="13012|A009900003|38173|B100600883|20120510|26547|5|4" class="goDetail">
						<td class="num">4</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									I.D.E.A 과정을 통한 발명교육 활성화 방안
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">109</td>
					</tr>
				
					<tr id="13012|A009900003|38172|B100600883|20120510|26546|6|3" class="goDetail">
						<td class="num">3</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									창의적인 구조물 제작 지도 방법에 관한 연구
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>1</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">123</td>
					</tr>
				
					<tr id="13012|A009900003|38171|B100600883|20120510|26545|7|2" class="goDetail">
						<td class="num">2</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									창의력챔피언대회는 학생들의 창의력 신장에 어떤 영향을 끼치는가?
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>2</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">60</td>
					</tr>
				
					<tr id="13012|A009900003|38170|B100600883|20120510|26525|8|1" class="goDetail">
						<td class="num">1</td>
						<td><span class="th_title">지역</span>전국</td>
						<td>
							<span class="th_title">자료명</span>
							<span class="td_w239">
								<a href="#" class="goMobDetail">
									대한민국학생창의력챔피언대회 참가를 통한 창의적 문제해결 능력 신장
									
								</a>
							</span>					
						</td>
						<td><span class="th_title">대회명</span>11년 전국교원발명교육연구대회</td>
						<td class="line2"><span class="th_title">등급</span>3</td>
						<td class="line2"><span class="th_title">학교급</span>전체</td>
						<td class="line2"><span class="th_title">교과</span>비교과</td>
						<td class="line2"><span class="th_title">등록일</span>2012-02-21</td>
						<td class="num">51</td>
					</tr>
				
			
			
		
	</tbody>
</table>

<div class="bbs_btn">
	<a title="등록안내" class="button" href="#none" id="infoWrite"><span>전국대회 공시자료 등록안내</span></a>
	
		<a title="글쓰기" class="button" href="#none" id="confrWrite"><span><img src="../images/common/ico_button_write.png">연구자료 등록</span></a>
	
</div>


	
		<div class="pagingNav up noPageNav" id="pagingBar">
			
			
				
					<strong>1</strong>
					
				
			
			
		</div>
	



'''


bs_obj = BeautifulSoup(html, 'html.parser')

#soup select - 클래스의 span값이 ah_k인 것을 고르기
# title_list = bs_obj.select('.PM_CL_realtimeKeyword_rolling_base span[class*=ah_k]')

#태그이름과 클래스 이름 입력받아서 결과값을 파일로 저장하기
#todo 함수 밖에서 결과값을 파일로 저장하기
def edunetCrawl(_tag,_class):
    #soup select - a태그의 클래스가 'goMobDetail'인 것을 고르기
    title_list = bs_obj.select('' + _tag + '[class*=' + _class + ']')

    out = open('out.txt','a')

    for idx, title in enumerate(title_list,1): #넘버링, 순위매기기
        _a = print("{} {}{}{}".format('자료명',idx,'.',title.text.replace('\n','').strip()),file=out) #출력하기 - 폼에 맞게
    out.close()
    return(_a)

edunetCrawl('a','goMobDetail')
