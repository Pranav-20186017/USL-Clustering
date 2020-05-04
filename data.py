from selenium import webdriver
import pandas as pd

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
df = pd.DataFrame(columns=['Name','Synopsis','Genre'])
first_page = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&view=advanced"
driver.get(first_page)
for i in range(1,101):
	name = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/h3/a").text.strip()
	syn = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[2]").text.strip()
	try:
		gen = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[1]/span[5]").text.strip()
	except Exception:
		gen = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[1]/span[3]").text.strip()
	print("name: {}".format(name))
	print("Synopsis: {}".format(syn))
	print("Genre: {}".format(gen))
	temp_df = pd.DataFrame([[name, syn, gen]], columns=['Name', 'Synopsis', 'Genre'])
	df = df.append(temp_df)
	print("--------------------------\n")
for i in range(101,902,100):
	remaining_pages = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(i)+"&ref_=adv_nxt"
	driver.get(remaining_pages)
	for i in range(1,101):
		name = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/h3/a").text.strip()
		syn = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[2]").text.strip()
		try:
			gen = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[1]/span[5]").text.strip()
		except Exception:
			gen = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div["+str(i)+"]/div[3]/p[1]/span[3]").text.strip()
		print("name: {}".format(name))
		print("Synopsis: {}".format(syn))
		print("Genre: {}".format(gen))
		temp_df = pd.DataFrame([[name, syn, gen]], columns=['Name', 'Synopsis', 'Genre'])
		df = df.append(temp_df)
		print("--------------------------\n")

print(df.shape)

driver.quit()

df.to_csv('IMDB Data.csv')





