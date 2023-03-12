
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
#import undetected_chromedriver as uc
import time

from helpers import urlScrapping, returnNumber, lastWord, lastTwoWord, isfloat
from funciones import insertTable, update_true_car_listings_table
from models import fuel, market_value, safety_rating, specifications_car, info_car, aditional_info_car, aditional_info_car_registrounico, info_car_registrounico

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--incognito")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument('--disable-notifications')
# chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--enable-javascript")
# chrome_options.add_argument("user-data-dir=selenium")

driver = webdriver.Chrome(chrome_options=chrome_options)

#driver = uc.Chrome()
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)
driver.get(urlScrapping)

# https://vincheckpro.com/
def vincheckpro(conn, Vin, Id):
    vinFind = driver.find_element(By.XPATH, "//*[@id='vin-search-input-1']")

    vinFind.send_keys(Vin)

    btn_buscar = driver.find_element(
        By.XPATH, "//*[@id='vin-search-form-1']/div/div[2]")
    action.move_to_element(btn_buscar).click().perform()

    time.sleep(30)

    # Market Value
    newMarketValue = market_value()
    tabla_market_value = driver.find_element(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[2]/div/div[3]/div/table")
    trCollection = tabla_market_value.find_elements(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[2]/div/div[3]/div/table/tbody/tr")

    if len(trCollection) > 0:
        #count_tr = 1
        # for element in trCollection:
        #data = f'//*[@id="post-4920"]/div/div/div/div[5]/div[2]/div/div[3]/div/table/tbody/tr[{count_tr}]/td'
        data = f'//*[@id="post-4920"]/div/div/div/div[5]/div[2]/div/div[3]/div/table/tbody/tr/td'
        tdCollection = driver.find_elements(By.XPATH, data)

        if len(tdCollection) > 0:
            newMarketValue.Vin = Vin
            newMarketValue.InvoicePrice = tdCollection[0].text.replace(",", "").split('$')[1]
            newMarketValue.BelowMarketPrice = tdCollection[1].text.replace(",", "").split('$')[1]
            newMarketValue.AverageMarketPrice = tdCollection[2].text.replace(",", "").split('$')[1]
            newMarketValue.AboveMarketPrice = tdCollection[3].text.replace(",", "").split('$')[1]

            insertTable(conn, newMarketValue)

    #time.sleep(3)

    # Fuel
    tabla_fuel = driver.find_element(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[4]/div/div[2]/div/table")
    trCollection_fuel = tabla_fuel.find_elements(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[4]/div/div[2]/div/table/tbody/tr")

    newFuel = fuel()
    #countfuel_tr = 1
    if len(trCollection_fuel) > 0:
        #data = f'//*[@id="post-4920"]/div/div/div/div[5]/div[4]/div/div[2]/div/table/tbody/tr[{countfuel_tr}]/td'
        data = f'//*[@id="post-4920"]/div/div/div/div[5]/div[4]/div/div[2]/div/table/tbody/tr/td'
        tdCollection_fuel = driver.find_elements(By.XPATH, data)

        if len(tdCollection_fuel) > 0:
            newFuel.Vin = Vin
            newFuel.CityMileage = returnNumber(tdCollection_fuel[0].text)
            newFuel.HighwayMileage = returnNumber(tdCollection_fuel[1].text)
            newFuel.FuelType = lastWord(tdCollection_fuel[2].text)
            newFuel.FuelCapacity = returnNumber(tdCollection_fuel[3].text)

            insertTable(conn, newFuel)
     
    #time.sleep(3)

    # Safety Rating
    tabla_safety_rating = driver.find_element(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[5]/div/div[2]/div/table")
    trCollection_safety_rating = tabla_safety_rating.find_elements(
        By.XPATH, "//*[@id='post-4920']/div/div/div/div[5]/div[5]/div/div[2]/div/table/tbody/tr")

    # countsafety_rating_tr = 2
    # for element in trCollection_safety_rating:

    newsafetyrating = safety_rating()
    if len(trCollection_safety_rating) > 0:
        data = f'//*[@id="post-4920"]/div/div/div/div[5]/div[5]/div/div[2]/div/table/tbody/tr/td'
        tdCollection_safetyrating = driver.find_elements(By.XPATH, data)

        if len(tdCollection_safetyrating) > 0:
            newsafetyrating.Vin = Vin
            if len(tdCollection_safetyrating) == 4:
                newsafetyrating.RoofStrengthTestResults = lastWord(tdCollection_safetyrating[0].text)
                newsafetyrating.RearCrashProtectionHeadRestraintRatings = lastWord(tdCollection_safetyrating[1].text)
                newsafetyrating.SmallOverlapFrontTestResults = lastWord(tdCollection_safetyrating[2].text)
                newsafetyrating.ModerateOverlapFrontTestResults = lastWord(tdCollection_safetyrating[3].text)
            if len(tdCollection_safetyrating) == 5:
                newsafetyrating.RoofStrengthTestResults = lastWord(tdCollection_safetyrating[0].text)
                newsafetyrating.RearCrashProtectionHeadRestraintRatings = lastWord(tdCollection_safetyrating[1].text)
                newsafetyrating.SmallOverlapFrontTestResults = lastWord(tdCollection_safetyrating[2].text)
                newsafetyrating.ModerateOverlapFrontTestResults = lastWord(tdCollection_safetyrating[3].text)   
                newsafetyrating.SideImpactTestResults = lastWord(tdCollection_safetyrating[4].text)

            insertTable(conn, newsafetyrating)

    #time.sleep(3)

    # specifications
    newspecifications = specifications_car()    
    element_li = driver.find_element(By.XPATH, "//*[@id='menu-item-10256']/a")
    action.move_to_element(element_li).click().perform()
    time.sleep(3)
                                                          
    tabla_specifications = driver.find_element(By.XPATH, "//*[@id='post-17578']/div/div/div/div[5]/div/div/div[2]/div/table[1]")
    trCollection_specifications = tabla_specifications.find_elements(
        By.XPATH, "//*[@id='post-17578']/div/div/div/div[5]/div/div/div[2]/div/table[1]/tbody/tr")
            
    
    count_specifications = 1
    find_trim = False
    find_country = False
    find_type = False
    find_size = False
    find_transmission = False
    find_doors = False
        
    for element in trCollection_specifications:                
        data = f'//*[@id="post-17578"]/div/div/div/div[5]/div/div/div[2]/div/table[1]/tbody/tr[{count_specifications}]/td'
        tdCollection_safetyrating = element.find_elements(By.XPATH, data)
        
        if len(tdCollection_safetyrating) > 0:
            newspecifications.Vin = Vin
            
            if(tdCollection_safetyrating[0].text.lower().find("trim") != -1 and find_trim == False):
                find_trim = True 
                newspecifications.TrimPremiumPackage = lastTwoWord(tdCollection_safetyrating[0].text)
                
            if(tdCollection_safetyrating[0].text.lower().find("country of origin") != -1 and find_country == False):    
                find_country = True
                newspecifications.CountryOrigin = lastTwoWord(tdCollection_safetyrating[0].text)
                
            if(tdCollection_safetyrating[0].text.lower().find("vehicle type") != -1 and find_type == False):  
                find_type = True  
                newspecifications.VehicleType = lastWord(tdCollection_safetyrating[0].text)

            if(tdCollection_safetyrating[0].text.lower().find("vehicle size") != -1 and find_size == False):  
                find_size = True  
                newspecifications.VehicleSize = lastWord(tdCollection_safetyrating[0].text)
                
            if(tdCollection_safetyrating[0].text.lower().find("transmission type") != -1 and find_transmission == False):  
                find_transmission = True  
                newspecifications.TransmissionType = lastWord(tdCollection_safetyrating[0].text) 
                
            if(tdCollection_safetyrating[0].text.lower().find("doors") != -1 and find_doors == False):  
                find_doors = True  
                newspecifications.TransmissionType = lastWord(tdCollection_safetyrating[0].text)        
                       
        count_specifications = count_specifications + 1
        
    insertTable(conn, newspecifications) 
    time.sleep(3)

    update_true_car_listings_table(conn, "true_car_listings", Id)

    #go to home
    driver.get(urlScrapping)
    time.sleep(3)
    
# https://vincheck.info/
def vincheck(conn, Vin, Id):

    # home
    btn_buscar = driver.find_element(
        By.XPATH, "//*[@id='content']/article/div/div/div/div[2]/div/div/div[1]/a")
    action.move_to_element(btn_buscar).click().perform()

    # https://vincheck.info/check/vin-check.php
    vinFind = driver.find_element(By.XPATH, "//*[@id='vin']")
    vinFind.send_keys(Vin)

    # https://vincheck.info/check/vin-check.php
    # btn buscar vin
    btn_buscar_vin = driver.find_element(
        By.XPATH, "//*[@id='frm']/div[2]/input")
    action.move_to_element(btn_buscar_vin).click().perform()
    time.sleep(10)

    # https://vincheck.info/check/vin-check-progress.php
    progress = driver.find_element(By.CSS_SELECTOR, "#myBar")
    # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#myBar")))
    progressCondition = progress.get_attribute('aria-valuenow')
    print(progressCondition)

    # https://vincheck.info/check/report-summary.php?vin=JH4CU26639C015787
    # market value li
    element_li = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[1]/aside/ul/li[2]/a")
    action.move_to_element(element_li).click().perform()

    driver.get(urlScrapping)



# https://driving-tests.org/vin-decoder
def drivingtests(conn, Vin, Id):
    vinFind = driver.find_element(By.XPATH, "//*[@id='vin_input']")
    vinFind.send_keys(Vin)

    # recaptcha
    # try:
    #     btn_buscar = driver.find_element(By.XPATH, "//*[@id='submit_vin']")
    #     action.move_to_element(btn_buscar).click().perform()

    #     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/anchor')]")))
    #     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']/div[1]"))).click()

    # except Exception as e:
    #     print(e.msg)

    btn_buscar = driver.find_element(By.XPATH, "//*[@id='submit_vin']")
    action.move_to_element(btn_buscar).click().perform()
    time.sleep(5)
    
    # tabla main
    newinfocar = info_car()
    tabla_main = driver.find_element(By.XPATH, "//*[@id='report_main']/div[2]/table")
    trCollection = tabla_main.find_elements(By.XPATH, "//*[@id='report_main']/div[2]/table/tbody/tr")
    
    if len(trCollection) > 0:
        count_specifications = 0
        newinfocar.Vin = Vin
             
        for element in trCollection:
            count_specifications += 1
            data = f'//*[@id="report_main"]/div[2]/table/tbody/tr[{count_specifications}]/td'
            tdCollection_info = element.find_elements(By.XPATH, data)
        
            if len(tdCollection_info) > 0:
               
                if(tdCollection_info[0].text.lower().find("manufactured by") != -1):
                   newinfocar.Manufactured = tdCollection_info[1].text.lower()
                
                if(tdCollection_info[0].text.lower().find("plant company name") != -1):
                    newinfocar.Plant_Company_Name = tdCollection_info[1].text.lower()  
                
                if(tdCollection_info[0].text.lower().find("vehicle type") != -1):
                    newinfocar.Vehicle_Type = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("series") != -1):
                    newinfocar.Series = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("body class") != -1):
                    newinfocar.Body_Class = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("doors") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Doors = int(tdCollection_info[1].text.lower())
            
                if(tdCollection_info[0].text.lower().find("front airbag location") != -1):
                    newinfocar.Front_Airbag_Location = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("seat belts type") != -1):
                    newinfocar.Seat_Belts_Type = tdCollection_info[1].text.lower()
                
                if(tdCollection_info[0].text.lower().find("engine displacement (ci)") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Engine_Displacement_CI = float(tdCollection_info[1].text.lower())
                
                if(tdCollection_info[0].text.lower().find("engine displacement (cc)") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Engine_Displacement_CC = float(tdCollection_info[1].text.lower())
                                
                if(tdCollection_info[0].text.lower().find("fuel type") != -1):
                    newinfocar.Fuel_Type = tdCollection_info[1].text.lower()  
            
                if(tdCollection_info[0].text.lower().find("engine number of cylinders") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Engine_Number_Cylinders = int(tdCollection_info[1].text.lower())
    
        insertTable(conn, newinfocar)
    
    #Additional Vehicle Info
    newaditionalinfocar = aditional_info_car()           
   
    tabla_detalle = driver.find_element(By.XPATH, "//*[@id='report_extra']/div[2]/table")
    trCollection_detalle = tabla_detalle.find_elements(By.XPATH, "//*[@id='report_extra']/div[2]/table/tbody/tr")

    if len(trCollection_detalle) > 0:
        count_detalle = 0
        newaditionalinfocar.Vin = Vin
             
        for element in trCollection_detalle:
            count_detalle += 1            
            data = f'//*[@id="report_extra"]/div[2]/table/tbody/tr[{count_detalle}]/td'
            tdCollection_detalle = driver.find_elements(By.XPATH, data)

            if len(tdCollection_detalle) > 0:
                                
                if(tdCollection_detalle[0].text.lower().find("bed type") != -1):
                    newaditionalinfocar.Bed_Type = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("cab type") != -1):
                    newaditionalinfocar.Cab_Type = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("engine model") != -1):
                    newaditionalinfocar.Engine_Model = tdCollection_detalle[1].text.lower()                         

                if(tdCollection_detalle[0].text.lower().find("engine power (kw)") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newaditionalinfocar.Engine_Power = float(tdCollection_detalle[1].text.lower())
                    
                if(tdCollection_detalle[0].text.lower().find("gross vehicle weight rating from") != -1):
                    newaditionalinfocar.Vehicle_Weight = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("transmission style") != -1):
                    newaditionalinfocar.Transmission_Style = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("trim") != -1):
                    newaditionalinfocar.Trim = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("curtain air bag locations") != -1):
                    newaditionalinfocar.Air_Bag_Locations = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("valve train design") != -1):
                    newaditionalinfocar.Valve_Train_Design = tdCollection_detalle[1].text.lower()
                
                if(tdCollection_detalle[0].text.lower().find("transmission speeds") != -1):
                    newaditionalinfocar.Transmission_Speeds = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("engine configuration") != -1):
                    newaditionalinfocar.Engine_Configuration = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("engine manufacturer") != -1):
                    newaditionalinfocar.Engine_Manufacturer = tdCollection_detalle[1].text.lower()                         
                                                          
        insertTable(conn, newaditionalinfocar)

    update_true_car_listings_table(conn, "true_car_listings", Id)
    
    driver.get(urlScrapping)
    
    
def drivingtestsregistroUnico(conn, Vin, Id):
    vinFind = driver.find_element(By.XPATH, "//*[@id='vin_input']")
    vinFind.send_keys(Vin)

    btn_buscar = driver.find_element(By.XPATH, "//*[@id='submit_vin']")
    action.move_to_element(btn_buscar).click().perform()
    time.sleep(5)
    
    # tabla main
    newinfocar = info_car_registrounico()
    tabla_main = driver.find_element(By.XPATH, "//*[@id='report_main']/div[2]/table")
    trCollection = tabla_main.find_elements(By.XPATH, "//*[@id='report_main']/div[2]/table/tbody/tr")
    
    if len(trCollection) > 0:
        count_specifications = 0
        newinfocar.Vin = Vin
             
        for element in trCollection:
            count_specifications += 1
            data = f'//*[@id="report_main"]/div[2]/table/tbody/tr[{count_specifications}]/td'
            tdCollection_info = element.find_elements(By.XPATH, data)
        
            if len(tdCollection_info) > 0:
               
                if(tdCollection_info[0].text.lower().find("manufactured by") != -1):
                   newinfocar.Manufactured = tdCollection_info[1].text.lower()
                
                if(tdCollection_info[0].text.lower().find("plant company name") != -1):
                    newinfocar.Plant_Company_Name = tdCollection_info[1].text.lower()  
                
                if(tdCollection_info[0].text.lower().find("vehicle type") != -1):
                    newinfocar.Vehicle_Type = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("series") != -1):
                    newinfocar.Series = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("body class") != -1):
                    newinfocar.Body_Class = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("doors") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Doors = int(tdCollection_info[1].text.lower())
            
                if(tdCollection_info[0].text.lower().find("front airbag location") != -1):
                    newinfocar.Front_Airbag_Location = tdCollection_info[1].text.lower()
            
                if(tdCollection_info[0].text.lower().find("seat belts type") != -1):
                    newinfocar.Seat_Belts_Type = tdCollection_info[1].text.lower()
                
                if(tdCollection_info[0].text.lower().find("engine displacement (ci)") != -1):
                    if(tdCollection_info[1].text.isnumeric() or isfloat(tdCollection_info[1].text)):
                        newinfocar.Engine_Displacement_CI = float(tdCollection_info[1].text.lower())
                
                if(tdCollection_info[0].text.lower().find("engine displacement (cc)") != -1):
                    if(tdCollection_info[1].text.isnumeric() or isfloat(tdCollection_info[1].text)):
                        newinfocar.Engine_Displacement_CC = float(tdCollection_info[1].text.lower())
                                
                if(tdCollection_info[0].text.lower().find("fuel type") != -1):
                    newinfocar.Fuel_Type = tdCollection_info[1].text.lower()  
            
                if(tdCollection_info[0].text.lower().find("engine number of cylinders") != -1):
                    if(tdCollection_info[1].text.isnumeric()):
                        newinfocar.Engine_Number_Cylinders = int(tdCollection_info[1].text.lower())
    
        insertTable(conn, newinfocar)
    
    #Additional Vehicle Info
    newaditionalinfocar = aditional_info_car_registrounico()           
   
    tabla_detalle = driver.find_element(By.XPATH, "//*[@id='report_extra']/div[2]/table")
    trCollection_detalle = tabla_detalle.find_elements(By.XPATH, "//*[@id='report_extra']/div[2]/table/tbody/tr")

    if len(trCollection_detalle) > 0:
        count_detalle = 0
        newaditionalinfocar.Vin = Vin
             
        for element in trCollection_detalle:
            count_detalle += 1            
            data = f'//*[@id="report_extra"]/div[2]/table/tbody/tr[{count_detalle}]/td'
            tdCollection_detalle = driver.find_elements(By.XPATH, data)

            if len(tdCollection_detalle) > 0:
                                
                if(tdCollection_detalle[0].text.lower().find("bed type") != -1):
                    newaditionalinfocar.Bed_Type = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("cab type") != -1):
                    newaditionalinfocar.Cab_Type = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("engine model") != -1):
                    newaditionalinfocar.Engine_Model = tdCollection_detalle[1].text.lower()                         

                if(tdCollection_detalle[0].text.lower().find("engine power (kw)") != -1):
                    if(tdCollection_info[1].text.isnumeric() or isfloat(tdCollection_detalle[1].text)):
                        newaditionalinfocar.Engine_Power = float(tdCollection_detalle[1].text.lower())
                    
                if(tdCollection_detalle[0].text.lower().find("gross vehicle weight rating from") != -1):
                    newaditionalinfocar.Vehicle_Weight = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("transmission style") != -1):
                    newaditionalinfocar.Transmission_Style = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("trim") != -1):
                    newaditionalinfocar.Trim = tdCollection_detalle[1].text.lower() 
                    
                if(tdCollection_detalle[0].text.lower().find("curtain air bag locations") != -1 or
                   tdCollection_detalle[0].text.lower().find("side air bag locations") != -1):
                    newaditionalinfocar.Air_Bag_Locations = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("valve train design") != -1):
                    newaditionalinfocar.Valve_Train_Design = tdCollection_detalle[1].text.lower()
                
                if(tdCollection_detalle[0].text.lower().find("transmission speeds") != -1):
                    newaditionalinfocar.Transmission_Speeds = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("engine configuration") != -1):
                    newaditionalinfocar.Engine_Configuration = tdCollection_detalle[1].text.lower()
                    
                if(tdCollection_detalle[0].text.lower().find("engine manufacturer") != -1):
                    newaditionalinfocar.Engine_Manufacturer = tdCollection_detalle[1].text.lower()                         
                                                          
        insertTable(conn, newaditionalinfocar)

    update_true_car_listings_table(conn, "registro_unico_vin", Id)
    
    driver.get(urlScrapping)    


